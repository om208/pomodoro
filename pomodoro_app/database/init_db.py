import sqlite3

def initialize_db():
    conn = sqlite3.connect('pomodoro_app.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS allTask (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        description TEXT,
        task_deadline TEXT,
        estimate_time TEXT,
        priority TEXT DEFAULT 'medium',
        remainder_time_interval TEXT DEFAULT '30Minute',
        remainder_sound TEXT DEFAULT 'double beep sound',
        status TEXT,
        entry_date INTEGER DEFAULT (strftime('%s', 'now')),
        task_complete_date INTEGER
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Reminder (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task_id INTEGER,
        progress_status TEXT,
        efficiency REAL DEFAULT 6.0,
        food_consume BOOLEAN DEFAULT 0
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Progress_status_align (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        initial_2Minute_music_type TEXT DEFAULT 'Motivational',
        initial_2_minute_speech_folder_path TEXT DEFAULT 'Remainder/Status-align/initial-2miunte-speech/',
        core_speech_folder_path TEXT DEFAULT 'Remainder/Status-align/core-speech/',
        core_time_slot_time TEXT DEFAULT '5minutes',
        post_break_gap TEXT DEFAULT '10minutes',
        post_break_background_music_folder_path TEXT DEFAULT 'Remainder/Status-align/post-break-backgrund_music/vibrational/'
    )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_db()