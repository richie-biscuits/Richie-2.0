-- Mission Control v1.1.1
-- Board hierarchy support for Marrs multi-board flow

ALTER TABLE todos ADD COLUMN IF NOT EXISTS board_id TEXT DEFAULT 'default';
ALTER TABLE todos ADD COLUMN IF NOT EXISTS board_name TEXT DEFAULT 'Default Board';

-- Optional backfill for existing rows
UPDATE todos
SET board_id = COALESCE(board_id, 'default'),
    board_name = COALESCE(board_name, 'Default Board')
WHERE board_id IS NULL OR board_name IS NULL;
