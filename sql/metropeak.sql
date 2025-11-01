DROP TABLE IF EXISTS metro.property CASCADE;

CREATE TABLE IF NOT EXISTS metro.property (
            brokeredBy FLOAT,
            status TEXT,
            price FLOAT,
            bed FLOAT,
            bath FLOAT,
            acreLot FLOAT,
            street TEXT,
            city TEXT,
            state TEXT,
            zipcode TEXT,
            houseSize FLOAT
        );
   