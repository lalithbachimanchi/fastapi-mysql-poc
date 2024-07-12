from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel
import pymysql.cursors
from models import HealthCareData  # Import your Pydantic model


# Create FastAPI instance
app = FastAPI()

# MySQL connection configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'genaidb',
    'cursorclass': pymysql.cursors.DictCursor,
    'port': 3307
}

# Function to establish MySQL connection
def get_db_connection():
    return pymysql.connect(**db_config)

# Endpoint using the Pydantic model
@app.get("/healthcaredata/", response_model=List[HealthCareData])
async def get_healthcare_data():
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            sql = "SELECT * FROM health_care_data"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
    finally:
        connection.close()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

