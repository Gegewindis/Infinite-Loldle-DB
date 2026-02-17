--History
DELIMITER //
CREATE TRIGGER log_game
BEFORE UPDATE ON Users
FOR EACH ROW
BEGIN
    INSERT INTO ChangeLog (score, changeType, changeTime, username)
    VALUES (NEW.points - OLD.points,
    'admin',
    NOW(),
    NEW.Username);
END //

DELIMITER ;