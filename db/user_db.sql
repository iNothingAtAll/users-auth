-- =============================================
-- BASE DE DATOS - CASA DE APUESTAS DEPORTIVAS
-- =============================================

CREATE TABLE IF NOT EXISTS usuarios (
    id                INTEGER PRIMARY KEY AUTO_INCREMENT,   
    nombre           TEXT NOT NULL UNIQUE,
    nombre_publico    TEXT NOT NULL,
    correo            TEXT NOT NULL UNIQUE,
    telefono          TEXT,
    password_hash     TEXT NOT NULL,
    saldo             REAL DEFAULT 0.0,
    fecha_registro    DATETIME DEFAULT CURRENT_TIMESTAMP,
    activo            INTEGER DEFAULT 1
);

CREATE TABLE IF NOT EXISTS transacciones (
    id           INTEGER PRIMARY KEY AUTO_INCREMENT,
    id_usuario   INTEGER NOT NULL,
    tipo         TEXT NOT NULL,        -- deposito, retiro, ganancia, perdida
    monto        REAL NOT NULL,
    fecha        DATETIME DEFAULT CURRENT_TIMESTAMP,
    descripcion  TEXT,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id)
);

CREATE TABLE IF NOT EXISTS apuestas (
    id            INTEGER PRIMARY KEY AUTO_INCREMENT,
    id_usuario    INTEGER NOT NULL,
    id_evento_api TEXT NOT NULL,        -- el id que viene de la API externa
    tipo_evento   TEXT NOT NULL,        -- "profesional" o "universitario"
    monto         REAL NOT NULL,
    prediccion    TEXT NOT NULL,
    cuota         REAL NOT NULL,
    estado        TEXT DEFAULT 'pendiente',
    fecha         DATETIME DEFAULT CURRENT_TIMESTAMP,
    ganancia      REAL DEFAULT 0.0,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id)
);



CREATE TABLE IF NOT EXISTS sesiones (
    id           INTEGER PRIMARY KEY AUTO_INCREMENT,
    id_usuario   INTEGER NOT NULL,
    token        TEXT NOT NULL UNIQUE,
    fecha_inicio DATETIME DEFAULT CURRENT_TIMESTAMP,
    fecha_expira DATETIME NOT NULL,
    activo       INTEGER DEFAULT 1,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id)
);

CREATE TABLE IF NOT EXISTS bonos (
    id           INTEGER PRIMARY KEY AUTO_INCREMENT,
    id_usuario   INTEGER NOT NULL,
    tipo         TEXT NOT NULL,        -- "bienvenida", "recarga", "fidelidad"
    monto        REAL NOT NULL,
    usado        INTEGER DEFAULT 0,
    fecha_expira DATETIME NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id)
);