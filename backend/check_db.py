import sqlite3

DB_PATH = 'ai_manager.db'

def check_devices():
    """连接到数据库并打印出devices表中的所有记录"""
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        print("--- 查询 devices 表中的所有记录 ---")
        cursor.execute("SELECT * FROM devices")
        rows = cursor.fetchall()
        
        if not rows:
            print("devices 表中没有任何记录。")
            return

        for row in rows:
            print("\n--- 设备记录 ---")
            for key in row.keys():
                print(f"{key}: {row[key]}")
            
    except sqlite3.Error as e:
        print(f"数据库错误: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    check_devices()
