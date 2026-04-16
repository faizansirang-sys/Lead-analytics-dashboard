from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Lead
from datetime import datetime
import csv
import io

router = APIRouter()


@router.post("/upload-csv")
async def upload_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    """Upload a CSV file containing lead data."""

    content = await file.read()
    decoded = content.decode("utf-8")
    reader = csv.DictReader(io.StringIO(decoded))

    leads_added = 0

    for row in reader:
        try:
            lead = Lead(
                agent_name=row.get("Agent", ""),
                source=row.get("Source", ""),
                status=row.get("Status", ""),
                revenue=float(row.get("Revenue", 0)),
                created_at=datetime.now()   # auto timestamp
            )

            db.add(lead)
            leads_added += 1

        except Exception as e:
            print("Row error:", e)

    db.commit()

    return {"message": f"Successfully uploaded {leads_added} leads"}