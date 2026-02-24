import csv
import random
from datetime import datetime, timedelta

NUM_RECORDS = 1_000_000_0

cities = ["Chennai", "Mumbai", "Delhi", "Bangalore", "Hyderabad"]
states = ["TN", "MH", "DL", "KA", "TS"]
categories = ["Electronics", "Fashion", "Grocery", "Beauty", "Appliances"]
payment_methods = ["UPI", "Credit Card", "Debit Card", "COD", "Wallet"]
order_statuses = ["Delivered", "Cancelled", "Returned"]
devices = ["Android", "iOS", "Web"]
traffic_sources = ["Google", "Instagram", "Facebook", "Direct"]

with open("ecommerce_10M_55cols.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow(
        [
            "transaction_id",
            "user_id",
            "first_name",
            "last_name",
            "age",
            "gender",
            "phone",
            "email",
            "city",
            "state",
            "pincode",
            "registration_date",
            "order_id",
            "order_date",
            "order_status",
            "order_channel",
            "product_id",
            "product_name",
            "category",
            "quantity",
            "price_per_unit",
            "total_price",
            "discount",
            "tax",
            "final_price",
            "payment_method",
            "payment_status",
            "transaction_ref",
            "bank_name",
            "card_type",
            "shipment_id",
            "warehouse_id",
            "courier_partner",
            "shipment_date",
            "delivery_date",
            "delivery_status",
            "return_requested",
            "return_reason",
            "device_type",
            "browser",
            "ip_address",
            "session_duration",
            "traffic_source",
            "campaign_name",
            "coupon_code",
            "loyalty_points",
            "customer_rating",
            "is_prime_user",
            "fraud_score",
            "is_high_risk",
            "latitude",
            "longitude",
            "currency",
            "emi_option",
            "gift_wrap",
            "referral_code",
        ]
    )

    for i in range(1, NUM_RECORDS + 1):
        user_id = random.randint(1, 100000)
        first = f"User{i}"
        last = f"LN{i}"
        age = random.randint(18, 70)
        gender = random.choice(["M", "F"])
        phone = random.randint(6000000000, 9999999999)
        email = f"user{i}@mail.com"
        city = random.choice(cities)
        state = random.choice(states)
        pincode = random.randint(600000, 699999)
        reg_date = datetime.now() - timedelta(days=random.randint(100, 2000))

        order_id = random.randint(100000, 999999)
        order_date = datetime.now() - timedelta(days=random.randint(0, 1000))
        order_status = random.choice(order_statuses)
        order_channel = random.choice(["App", "Web"])

        product_id = random.randint(1, 1000)
        product_name = f"Product{product_id}"
        category = random.choice(categories)
        quantity = random.randint(1, 5)
        price = round(random.uniform(100, 5000), 2)
        total = round(quantity * price, 2)

        discount = round(total * random.uniform(0, 0.3), 2)
        tax = round(total * 0.05, 2)
        final = round(total - discount + tax, 2)

        payment_method = random.choice(payment_methods)
        payment_status = random.choice(["Success", "Failed"])
        transaction_ref = f"TXN{i}"
        bank_name = random.choice(["HDFC", "SBI", "ICICI"])
        card_type = random.choice(["Visa", "Mastercard", "RuPay"])

        shipment_id = f"SHP{i}"
        warehouse_id = random.randint(1, 50)
        courier = random.choice(["Delhivery", "BlueDart", "DTDC"])
        shipment_date = order_date + timedelta(days=1)
        delivery_date = shipment_date + timedelta(days=random.randint(1, 7))
        delivery_status = random.choice(["On Time", "Delayed"])

        return_requested = random.choice(["Yes", "No"])
        return_reason = random.choice(["Damaged", "Wrong Item", "NA"])

        device_type = random.choice(devices)
        browser = random.choice(["Chrome", "Safari", "Edge"])
        ip_address = f"192.168.{random.randint(0,255)}.{random.randint(0,255)}"
        session_duration = random.randint(1, 60)

        traffic = random.choice(traffic_sources)
        campaign = f"Camp{random.randint(1,10)}"
        coupon = f"DISC{random.randint(1,50)}"

        loyalty = random.randint(0, 5000)
        rating = random.randint(1, 5)

        is_prime = random.choice(["Yes", "No"])
        fraud_score = round(random.uniform(0, 1), 2)
        is_high_risk = random.choice(["Yes", "No"])

        latitude = round(random.uniform(8.0, 37.0), 6)
        longitude = round(random.uniform(68.0, 97.0), 6)

        currency = "INR"
        emi_option = random.choice(["Yes", "No"])
        gift_wrap = random.choice(["Yes", "No"])
        referral = f"REF{random.randint(1000,9999)}"

        writer.writerow(
            [
                i,
                user_id,
                first,
                last,
                age,
                gender,
                phone,
                email,
                city,
                state,
                pincode,
                reg_date.strftime("%Y-%m-%d"),
                order_id,
                order_date.strftime("%Y-%m-%d"),
                order_status,
                order_channel,
                product_id,
                product_name,
                category,
                quantity,
                price,
                total,
                discount,
                tax,
                final,
                payment_method,
                payment_status,
                transaction_ref,
                bank_name,
                card_type,
                shipment_id,
                warehouse_id,
                courier,
                shipment_date.strftime("%Y-%m-%d"),
                delivery_date.strftime("%Y-%m-%d"),
                delivery_status,
                return_requested,
                return_reason,
                device_type,
                browser,
                ip_address,
                session_duration,
                traffic,
                campaign,
                coupon,
                loyalty,
                rating,
                is_prime,
                fraud_score,
                is_high_risk,
                latitude,
                longitude,
                currency,
                emi_option,
                gift_wrap,
                referral,
            ]
        )

print("10M records with 55 columns generated successfully.")
