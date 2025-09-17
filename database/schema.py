# database/schema.py
SCHEMA = """
PRAGMA foreign_keys = ON;

-- Users
CREATE TABLE IF NOT EXISTS user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT NOT NULL UNIQUE,
  password_hash TEXT NOT NULL,
  email TEXT NOT NULL,
  name TEXT
);

-- Employee category
CREATE TABLE IF NOT EXISTS employee_category (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL UNIQUE,
  description TEXT
);

-- Employees (Administrator/Operator/Technician via employee_type)
CREATE TABLE IF NOT EXISTS employee (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  email TEXT NOT NULL,
  employee_type TEXT NOT NULL CHECK (employee_type IN ('ADMINISTRATOR','OPERATOR','TECHNICIAN')),
  employee_category_id INTEGER,
  user_id INTEGER,
  FOREIGN KEY (employee_category_id) REFERENCES employee_category(id),
  FOREIGN KEY (user_id) REFERENCES user(id)
);

-- Clients
CREATE TABLE IF NOT EXISTS client (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  email TEXT NOT NULL,
  phone TEXT,
  address TEXT
);

-- Service taxonomy
CREATE TABLE IF NOT EXISTS category (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  description TEXT
);

CREATE TABLE IF NOT EXISTS service (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  description TEXT,
  category_id INTEGER,
  FOREIGN KEY (category_id) REFERENCES category(id)
);

-- Equipment
CREATE TABLE IF NOT EXISTS equipment_category (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  description TEXT
);

CREATE TABLE IF NOT EXISTS equipment (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  serial TEXT NOT NULL,
  equipment_category_id INTEGER,
  FOREIGN KEY (equipment_category_id) REFERENCES equipment_category(id)
);

-- Teams
CREATE TABLE IF NOT EXISTS team (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  description TEXT
);

CREATE TABLE IF NOT EXISTS team_employee (
  team_id INTEGER NOT NULL,
  employee_id INTEGER NOT NULL,
  PRIMARY KEY (team_id, employee_id),
  FOREIGN KEY (team_id) REFERENCES team(id) ON DELETE CASCADE,
  FOREIGN KEY (employee_id) REFERENCES employee(id) ON DELETE CASCADE
);

-- Tickets
CREATE TABLE IF NOT EXISTS ticket (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  client_id INTEGER NOT NULL,
  reporter_employee_id INTEGER,
  team_id INTEGER,
  state TEXT NOT NULL CHECK (state IN ('OPEN','IN_PROGRESS','RESOLVED','CLOSED')),
  created_at TEXT NOT NULL,
  FOREIGN KEY (client_id) REFERENCES client(id),
  FOREIGN KEY (reporter_employee_id) REFERENCES employee(id),
  FOREIGN KEY (team_id) REFERENCES team(id)
);

CREATE TABLE IF NOT EXISTS ticket_employee (
  ticket_id INTEGER NOT NULL,
  employee_id INTEGER NOT NULL,
  PRIMARY KEY (ticket_id, employee_id),
  FOREIGN KEY (ticket_id) REFERENCES ticket(id) ON DELETE CASCADE,
  FOREIGN KEY (employee_id) REFERENCES employee(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS ticket_service (
  ticket_id INTEGER NOT NULL,
  service_id INTEGER NOT NULL,
  PRIMARY KEY (ticket_id, service_id),
  FOREIGN KEY (ticket_id) REFERENCES ticket(id) ON DELETE CASCADE,
  FOREIGN KEY (service_id) REFERENCES service(id) ON DELETE CASCADE
);

-- Incidents
CREATE TABLE IF NOT EXISTS incident (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  ticket_id INTEGER NOT NULL,
  description TEXT NOT NULL,
  date TEXT NOT NULL,
  FOREIGN KEY (ticket_id) REFERENCES ticket(id)
);

-- Messages
CREATE TABLE IF NOT EXISTS message (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  ticket_id INTEGER NOT NULL,
  sender_employee_id INTEGER NOT NULL,
  date TEXT NOT NULL,
  content TEXT NOT NULL,
  FOREIGN KEY (ticket_id) REFERENCES ticket(id),
  FOREIGN KEY (sender_employee_id) REFERENCES employee(id)
);

-- Work logs
CREATE TABLE IF NOT EXISTS worklog (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  technician_employee_id INTEGER NOT NULL,
  ticket_id INTEGER NOT NULL,
  start_at TEXT,
  end_at TEXT,
  notes TEXT,
  FOREIGN KEY (technician_employee_id) REFERENCES employee(id),
  FOREIGN KEY (ticket_id) REFERENCES ticket(id)
);

-- Helpful indexes
CREATE INDEX IF NOT EXISTS idx_employee_type ON employee(employee_type);
CREATE INDEX IF NOT EXISTS idx_ticket_client ON ticket(client_id);
CREATE INDEX IF NOT EXISTS idx_ticket_state ON ticket(state);
CREATE INDEX IF NOT EXISTS idx_incident_ticket ON incident(ticket_id);
CREATE INDEX IF NOT EXISTS idx_message_ticket ON message(ticket_id);
"""
