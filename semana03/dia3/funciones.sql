use db_colegio
-- FUNCIONES

DELIMITER $$

CREATE FUNCTION fn_contar_cursos()
  RETURNS INT UNSIGNED
BEGIN
  DECLARE total INT UNSIGNED;
  SELECT COUNT(*) INTO total FROM tbl_alumno;
  RETURN total;
END
$$

DELIMITER ;

SELECT fn_contar_cursos();