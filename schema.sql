CREATE TABLE IF NOT EXISTS PresenterInfo (
    PresenterID INTEGER PRIMARY KEY AUTOINCREMENT,
    Author TEXT,
    Institution TEXT,
    Email TEXT,
    Title TEXT,
    Section INTEGER,
    Year INTEGER,
    File BLOB
    );

CREATE TABLE IF NOT EXISTS Admin (
    AdminID INTEGER PRIMARY KEY AUTOINCREMENT,
    Username TEXT,
    Password TEXT
    );