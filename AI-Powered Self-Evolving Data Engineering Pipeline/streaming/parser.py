import base64
import struct
from datetime import date, timedelta


class DebeziumParser:

    @staticmethod
    def parse(message):

        payload = message["payload"]

        after = payload["after"]

        if after is None:
            return None

        # ---------- Decode Decimal ----------

        if after.get("price"):

            raw = base64.b64decode(after["price"])

            value = int.from_bytes(
                raw,
                byteorder="big",
                signed=True
            )

            after["price"] = value / 100

        # ---------- Decode Date ----------

        if after.get("order_date"):

            epoch = date(1970, 1, 1)

            after["order_date"] = str(
                epoch + timedelta(days=after["order_date"])
            )

        return after