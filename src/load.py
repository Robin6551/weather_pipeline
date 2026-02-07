from sqlalchemy import create_engine, text
from datetime import datetime
from .config import DB_URL


engine = create_engine(DB_URL)

def upsert_dim_location(dim_location: dict) -> int:
    """
   insert or update dim_location and return location_id
    """
    sql = text("""
            INSERT INTO dim_location (city, country, latitude, longitude)
        VALUES (:city, :country, :latitude, :longitude)
        ON CONFLICT (city, country)
        DO UPDATE SET
            latitude = EXCLUDED.latitude,
            longitude = EXCLUDED.longitude
        RETURNING location_id;
    """
    )

    with engine.begin() as conn:
        result = conn.execute(sql, dim_location)
        location_id = result.fetchone()[0]
    return location_id

def insert_fact_weather(fact_weather: dict,location_id: int):
    """
   insert weather fact(append-only)
    """

    sql = text("""
      INSERT INTO fact_weather (
            location_id,
            observed_at,
            temperature,
            humidity,
            pressure,
            weather_main,
            weather_description,
            ingestion_time
        )
        VALUES (
            :location_id,
            :observed_at,
            :temperature,
            :humidity,
            :pressure,
            :weather_main,
            :weather_description,
            :ingestion_time
        );
""")
    
    payload = {
        **fact_weather,
        'location_id' : location_id,
        'ingestion_time': datetime.utcnow()
    }

    with engine.begin() as conn:
        conn.execute(sql, payload)


 
