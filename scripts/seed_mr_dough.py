from datetime import UTC, datetime
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from utils import database as db


BRAND_ID = "mr_dough"
BRAND_NAME = "Mr. Dough"
VANILLA_SUBMENU = "Vanilla Custard Doughnut"
MILKY_SUBMENU = "Milky Doughnut"

BRAND = {
    "business_name": BRAND_NAME,
    "tagline": "Premium Vanilla Custard Doughnuts",
    "role": "seller",
    "verified": True,
}

PRODUCTS = [
    {
        "id": "mr_dough_single_custard_doughnut",
        "name": "Single Custard Doughnut",
        "price": 500,
        "description": "Premium Vanilla Custard Doughnut",
        "sku": "MRD-SINGLE",
        "amount_in_stock": 20,
        "category": VANILLA_SUBMENU,
    },
    {
        "id": "mr_dough_pack_of_3_doughnuts",
        "name": "Pack of 3 Doughnuts",
        "price": 1400,
        "description": "Pack of 3 Premium Vanilla Custard Doughnuts",
        "sku": "MRD-PACK-3",
        "amount_in_stock": 20,
        "category": VANILLA_SUBMENU,
    },
    {
        "id": "mr_dough_single_milky_doughnut",
        "name": "Single Milky Doughnut",
        "price": 500,
        "description": "Premium Milky Doughnut",
        "sku": "MRD-MILKY-SINGLE",
        "amount_in_stock": 20,
        "category": MILKY_SUBMENU,
    },
    {
        "id": "mr_dough_pack_of_3_milky_doughnuts",
        "name": "Pack of 3 Milky Doughnuts",
        "price": 1400,
        "description": "Pack of 3 Premium Milky Doughnuts",
        "sku": "MRD-MILKY-PACK-3",
        "amount_in_stock": 20,
        "category": MILKY_SUBMENU,
    },
]


def main():
    now = datetime.now(UTC).isoformat()

    db.sellers_collection.set_by_key(
        BRAND_ID,
        {
            **BRAND,
            "_id": BRAND_ID,
            "id": BRAND_ID,
            "updated_at": now,
        },
    )

    for product in PRODUCTS:
        product_id = product["id"]
        payload = {
            **product,
            "_id": product_id,
            "business_name": BRAND_NAME,
            "brand": BRAND_NAME,
            "brand_name": BRAND_NAME,
            "category_name": product.get("category"),
            "type": product.get("category"),
            "updated_at": now,
        }
        db.products_collection.set_by_key(product_id, payload)

    print(f"Seeded {BRAND_NAME} with {len(PRODUCTS)} products.")


if __name__ == "__main__":
    main()
