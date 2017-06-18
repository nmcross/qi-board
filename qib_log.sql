BEGIN TRANSACTION;
CREATE TABLE "qib_log" (
	`triggerid`	INTEGER,
	`timestamp`	REAL,
	`notes`	TEXT,
	PRIMARY KEY(`triggerid`,`timestamp`)
);
COMMIT;
