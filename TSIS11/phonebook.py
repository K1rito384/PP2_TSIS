
CREATE TABLE IF NOT EXISTS phonebook (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    phone VARCHAR(20) NOT NULL
);

CREATE OR REPLACE FUNCTION get_users_by_pattern(pattern TEXT)
RETURNS TABLE (id INT, username VARCHAR, phone TEXT) AS $$
BEGIN
    RETURN QUERY
    SELECT u.id, u.username, p.phone
    FROM users u
    JOIN phonebook p ON u.id = p.user_id
    WHERE u.username ILIKE '%' || pattern || '%' 
       OR p.phone ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE insert_or_update_user(p_username TEXT, p_phone TEXT)
LANGUAGE plpgsql AS $$
DECLARE
    uid INT;
BEGIN
    SELECT id INTO uid FROM users WHERE username = p_username;

    IF uid IS NULL THEN
        INSERT INTO users (username) VALUES (p_username) RETURNING id INTO uid;
        INSERT INTO user_scores (user_id) VALUES (uid);
        INSERT INTO phonebook (user_id, phone) VALUES (uid, p_phone);
    ELSE
        UPDATE phonebook SET phone = p_phone WHERE user_id = uid;
    END IF;
END;
$$;

CREATE OR REPLACE PROCEDURE insert_many_users(p_usernames TEXT[], p_phones TEXT[])
LANGUAGE plpgsql AS $$
DECLARE
    i INT := 1;
    uid INT;
BEGIN
    CREATE TEMP TABLE IF NOT EXISTS invalid_users (username TEXT, phone TEXT) ON COMMIT DROP;

    WHILE i <= array_length(p_usernames, 1) LOOP
        IF p_phones[i] !~ '^\+?[0-9]{10,15}$' THEN
            INSERT INTO invalid_users VALUES (p_usernames[i], p_phones[i]);
        ELSE
            SELECT id INTO uid FROM users WHERE username = p_usernames[i];

            IF uid IS NULL THEN
                INSERT INTO users (username) VALUES (p_usernames[i]) RETURNING id INTO uid;
                INSERT INTO user_scores (user_id) VALUES (uid);
                INSERT INTO phonebook (user_id, phone) VALUES (uid, p_phones[i]);
            ELSE
                UPDATE phonebook SET phone = p_phones[i] WHERE user_id = uid;
            END IF;
        END IF;
        i := i + 1;
    END LOOP;
END;
$$;
SELECT * FROM invalid_users;

CREATE OR REPLACE FUNCTION get_users_paged(p_limit INT, p_offset INT)
RETURNS TABLE (id INT, username TEXT, phone TEXT) AS $$
BEGIN
    RETURN QUERY
    SELECT u.id, u.username, p.phone
    FROM users u
    JOIN phonebook p ON u.id = p.user_id
    ORDER BY u.id
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE PROCEDURE delete_user_by_username_or_phone(p_input TEXT)
LANGUAGE plpgsql AS $$
DECLARE
    uid INT;
BEGIN
    SELECT u.id INTO uid
    FROM users u
    LEFT JOIN phonebook p ON u.id = p.user_id
    WHERE u.username = p_input OR p.phone = p_input;

    IF uid IS NOT NULL THEN
        DELETE FROM users WHERE id = uid;
    END IF;
END;
$$;
