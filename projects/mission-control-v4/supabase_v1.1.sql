-- Mission Control v1.1
-- Add ordering support for Kanban drag/drop
ALTER TABLE todos ADD COLUMN IF NOT EXISTS position INTEGER DEFAULT 0;

-- Optional: backfill nulls if any old rows exist
UPDATE todos SET position = 0 WHERE position IS NULL;
