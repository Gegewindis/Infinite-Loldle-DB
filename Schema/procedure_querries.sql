DELIMITER //

CREATE PROCEDURE AddPoints(
    IN p_username VARCHAR(20),
    IN p_points INT
)

BEGIN
    DECLARE latest_gameID INT;

    UPDATE users
    SET points = points + p_points
    WHERE username = p_username;

    SELECT gameID
    INTO latest_gameID
    FROM ChangeLog
    ORDER BY gameID DESC
    LIMIT 1;

    UPDATE ChangeLog
    SET changeType = 'website'
    WHERE gameID = latest_gameID;
END //

DELIMITER ;