const pgp = require('pg-promise')();

const db = pgp({
  host: 'db',
  port: 5432,
  database: 'postgres',
  user: 'dfHC*7kT\'D(6Hem+7q9ex|55%+/bKBcN6=8}vXk1^Mp!nS\'LJtP\\',
  password: 'lB/MGC:XulEm55@b&c*kec9=$xUy\\%%sJu1o2L3?Z3=op(Na&8mt'
});

module.exports = db;
