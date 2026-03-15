-- 03_insert_bonos.sql
-- 3 bonos de prueba para Uniesport

INSERT INTO bonos (id, id_usuario, tipo, monto, usado, fecha_expira) VALUES
  (1, 12, 'bienvenida', 20000.0, 0, '2025-12-31 23:59:59'),
  (2, 38, 'recarga', 15000.0, 1, '2025-09-30 23:59:59'),
  (3, 29, 'fidelidad', 30000.0, 0, '2026-03-01 23:59:59');