class Product:
    def __init__(self, id, title, description, price, discountPercentage, rating, stock, brand, category, thumbnail, images):
        self.id = id
        self.title = title
        self.description = description
        self.price = price
        self.discountPercentage = discountPercentage
        self.rating = rating
        self.stock = stock
        self.brand = brand
        self.category = category
        self.thumbnail = thumbnail
        self.images = images
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "discountPercentage": self.discountPercentage,
            "rating": self.rating,
            "stock": self.stock,
            "brand": self.brand,
            "category": self.category,
            "thumbnail": self.thumbnail,
            "images": self.images
        }

# Sample products data
products_data = [
    {
        "id": 1,
        "title": "iPhone 9",
        "description": "An apple mobile which is nothing like apple",
        "price": 549,
        "discountPercentage": 12.96,
        "rating": 4.69,
        "stock": 94,
        "brand": "Apple",
        "category": "smartphones",
        "thumbnail": "https://cdn.dummyjson.com/product-images/1/thumbnail.jpg",
        "images": [
            "https://cdn.dummyjson.com/product-images/1/1.jpg",
            "https://cdn.dummyjson.com/product-images/1/2.jpg",
            "https://cdn.dummyjson.com/product-images/1/3.jpg",
            "https://cdn.dummyjson.com/product-images/1/4.jpg",
            "https://cdn.dummyjson.com/product-images/1/thumbnail.jpg"
        ]
    },
    {
        "id": 2,
        "title": "iPhone X",
        "description": "SIM-Free, Model A19211 6.5-inch Super Retina HD display with OLED technology A12 Bionic chip with ...",
        "price": 899,
        "discountPercentage": 17.94,
        "rating": 4.44,
        "stock": 34,
        "brand": "Apple",
        "category": "smartphones",
        "thumbnail": "https://cdn.dummyjson.com/product-images/2/thumbnail.jpg",
        "images": [
            "https://cdn.dummyjson.com/product-images/2/1.jpg",
            "https://cdn.dummyjson.com/product-images/2/2.jpg",
            "https://cdn.dummyjson.com/product-images/2/3.jpg",
            "https://cdn.dummyjson.com/product-images/2/thumbnail.jpg"
        ]
    },
    {
        "id": 3,
        "title": "Samsung Universe 9",
        "description": "Samsung's new variant which goes beyond Galaxy to the Universe",
        "price": 1249,
        "discountPercentage": 15.46,
        "rating": 4.09,
        "stock": 36,
        "brand": "Samsung",
        "category": "smartphones",
        "thumbnail": "https://cdn.dummyjson.com/product-images/3/thumbnail.jpg",
        "images": [
            "https://cdn.dummyjson.com/product-images/3/1.jpg"
        ]
    },
    {
        "id": 4,
        "title": "OPPOF19",
        "description": "OPPO F19 is officially announced on April 2021.",
        "price": 280,
        "discountPercentage": 17.91,
        "rating": 4.3,
        "stock": 123,
        "brand": "OPPO",
        "category": "smartphones",
        "thumbnail": "https://cdn.dummyjson.com/product-images/4/thumbnail.jpg",
        "images": [
            "https://cdn.dummyjson.com/product-images/4/1.jpg",
            "https://cdn.dummyjson.com/product-images/4/2.jpg",
            "https://cdn.dummyjson.com/product-images/4/3.jpg",
            "https://cdn.dummyjson.com/product-images/4/4.jpg",
            "https://cdn.dummyjson.com/product-images/4/thumbnail.jpg"
        ]
    },
    {
        "id": 5,
        "title": "Huawei P30",
        "description": "Huawei's re-badged P30 Pro New Edition was officially unveiled yesterday in Germany and now the device has made its way to the UK.",
        "price": 499,
        "discountPercentage": 10.58,
        "rating": 4.09,
        "stock": 32,
        "brand": "Huawei",
        "category": "smartphones",
        "thumbnail": "https://cdn.dummyjson.com/product-images/5/thumbnail.jpg",
        "images": [
            "https://cdn.dummyjson.com/product-images/5/1.jpg",
            "https://cdn.dummyjson.com/product-images/5/2.jpg",
            "https://cdn.dummyjson.com/product-images/5/3.jpg"
        ]
    },
    {
        "id": 6,
        "title": "MacBook Pro",
        "description": "MacBook Pro 2021 with mini-LED display may launch between September, November",
        "price": 1749,
        "discountPercentage": 11.02,
        "rating": 4.57,
        "stock": 83,
        "brand": "Apple",
        "category": "laptops",
        "thumbnail": "https://cdn.dummyjson.com/product-images/6/thumbnail.png",
        "images": [
            "https://cdn.dummyjson.com/product-images/6/1.png",
            "https://cdn.dummyjson.com/product-images/6/2.jpg",
            "https://cdn.dummyjson.com/product-images/6/3.png",
            "https://cdn.dummyjson.com/product-images/6/4.jpg"
        ]
    },
    {
        "id": 7,
        "title": "Samsung Galaxy Book",
        "description": "Samsung Galaxy Book S (2020) Laptop With Intel Lakefield Chip, 8GB of RAM Launched",
        "price": 1499,
        "discountPercentage": 4.15,
        "rating": 4.25,
        "stock": 50,
        "brand": "Samsung",
        "category": "laptops",
        "thumbnail": "https://cdn.dummyjson.com/product-images/7/thumbnail.jpg",
        "images": [
            "https://cdn.dummyjson.com/product-images/7/1.jpg",
            "https://cdn.dummyjson.com/product-images/7/2.jpg",
            "https://cdn.dummyjson.com/product-images/7/3.jpg",
            "https://cdn.dummyjson.com/product-images/7/thumbnail.jpg"
        ]
    },
    {
        "id": 8,
        "title": "Microsoft Surface Laptop 4",
        "description": "Style and speed. Stand out on HD video calls backed by Studio Mics. Capture ideas on the vibrant touchscreen.",
        "price": 1499,
        "discountPercentage": 10.23,
        "rating": 4.43,
        "stock": 68,
        "brand": "Microsoft Surface",
        "category": "laptops",
        "thumbnail": "https://cdn.dummyjson.com/product-images/8/thumbnail.jpg",
        "images": [
            "https://cdn.dummyjson.com/product-images/8/1.jpg",
            "https://cdn.dummyjson.com/product-images/8/2.jpg",
            "https://cdn.dummyjson.com/product-images/8/3.jpg",
            "https://cdn.dummyjson.com/product-images/8/4.jpg",
            "https://cdn.dummyjson.com/product-images/8/thumbnail.jpg"
        ]
    },
    {
        "id": 9,
        "title": "Infinix INBOOK",
        "description": "Infinix Inbook X1 Ci3 10th 8GB 256GB 14 Win10 Grey – 1 Year Warranty",
        "price": 1099,
        "discountPercentage": 11.83,
        "rating": 4.54,
        "stock": 96,
        "brand": "Infinix",
        "category": "laptops",
        "thumbnail": "https://cdn.dummyjson.com/product-images/9/thumbnail.jpg",
        "images": [
            "https://cdn.dummyjson.com/product-images/9/1.jpg",
            "https://cdn.dummyjson.com/product-images/9/2.png",
            "https://cdn.dummyjson.com/product-images/9/3.png",
            "https://cdn.dummyjson.com/product-images/9/4.jpg",
            "https://cdn.dummyjson.com/product-images/9/thumbnail.jpg"
        ]
    },
    {
        "id": 10,
        "title": "HP Pavilion 15-DK1056WM",
        "description": "HP Pavilion 15-DK1056WM Gaming Laptop 10th Gen Core i5, 8GB, 256GB SSD, GTX 1650 4GB, Windows 10",
        "price": 1099,
        "discountPercentage": 6.18,
        "rating": 4.43,
        "stock": 89,
        "brand": "HP Pavilion",
        "category": "laptops",
        "thumbnail": "https://cdn.dummyjson.com/product-images/10/thumbnail.jpeg",
        "images": [
            "https://cdn.dummyjson.com/product-images/10/1.jpg",
            "https://cdn.dummyjson.com/product-images/10/2.jpg",
            "https://cdn.dummyjson.com/product-images/10/3.jpg",
            "https://cdn.dummyjson.com/product-images/10/thumbnail.jpeg"
        ]
    },
    {
        "id": 11,
        "title": "perfume Oil",
        "description": "Mega Discount, Impression of Acqua Di Gio by GiorgioArmani concentrated attar perfume Oil",
        "price": 13,
        "discountPercentage": 8.4,
        "rating": 4.26,
        "stock": 65,
        "brand": "Impression of Acqua Di Gio",
        "category": "fragrances",
        "thumbnail": "https://cdn.dummyjson.com/product-images/11/thumbnail.jpg",
        "images": [
            "https://cdn.dummyjson.com/product-images/11/1.jpg",
            "https://cdn.dummyjson.com/product-images/11/2.jpg",
            "https://cdn.dummyjson.com/product-images/11/3.jpg",
            "https://cdn.dummyjson.com/product-images/11/thumbnail.jpg"
        ]
    },
    {
        "id": 12,
        "title": "Brown Perfume",
        "description": "Royal_Mirage Sport Brown Perfume for Men & Women - 120ml",
        "price": 40,
        "discountPercentage": 15.66,
        "rating": 4,
        "stock": 52,
        "brand": "Royal_Mirage",
        "category": "fragrances",
        "thumbnail": "https://cdn.dummyjson.com/product-images/12/thumbnail.jpg",
        "images": [
            "https://cdn.dummyjson.com/product-images/12/1.jpg",
            "https://cdn.dummyjson.com/product-images/12/2.jpg",
            "https://cdn.dummyjson.com/product-images/12/3.png",
            "https://cdn.dummyjson.com/product-images/12/4.jpg",
            "https://cdn.dummyjson.com/product-images/12/thumbnail.jpg"
        ]
    },
    {
        "id": 13,
        "title": "Fog Scent Xpressio Perfume",
        "description": "Product details of Best Fog Scent Xpressio Perfume 100ml For Men cool long lasting perfumes for Men",
        "price": 13,
        "discountPercentage": 8.14,
        "rating": 4.59,
        "stock": 61,
        "brand": "Fog Scent Xpressio",
        "category": "fragrances",
        "thumbnail": "https://cdn.dummyjson.com/product-images/13/thumbnail.webp",
        "images": [
            "https://cdn.dummyjson.com/product-images/13/1.jpg",
            "https://cdn.dummyjson.com/product-images/13/2.png",
            "https://cdn.dummyjson.com/product-images/13/3.jpg",
            "https://cdn.dummyjson.com/product-images/13/4.jpg",
            "https://cdn.dummyjson.com/product-images/13/thumbnail.webp"
        ]
    },
    {
        "id": 14,
        "title": "Non-Alcoholic Concentrated Perfume Oil",
        "description": "Original Al Munakh® by Mahal Al Musk | Our Impression of Climate | 6ml Non-Alcoholic Concentrated Perfume Oil",
        "price": 120,
        "discountPercentage": 15.6,
        "rating": 4.21,
        "stock": 114,
        "brand": "Al Munakh",
        "category": "fragrances",
        "thumbnail": "https://cdn.dummyjson.com/product-images/14/thumbnail.jpg",
        "images": [
            "https://cdn.dummyjson.com/product-images/14/1.jpg",
            "https://cdn.dummyjson.com/product-images/14/2.jpg",
            "https://cdn.dummyjson.com/product-images/14/3.jpg",
            "https://cdn.dummyjson.com/product-images/14/thumbnail.jpg"
        ]
    },
    {
        "id": 15,
        "title": "Eau De Perfume Spray",
        "description": "Genuine  Al-Rehab spray perfume from UAE/Saudi Arabia/Yemen High Quality",
        "price": 30,
        "discountPercentage": 10.99,
        "rating": 4.7,
        "stock": 105,
        "brand": "Lord - Al-Rehab",
        "category": "fragrances",
        "thumbnail": "https://cdn.dummyjson.com/product-images/15/thumbnail.jpg",
        "images": [
            "https://cdn.dummyjson.com/product-images/15/1.jpg",
            "https://cdn.dummyjson.com/product-images/15/2.jpg",
            "https://cdn.dummyjson.com/product-images/15/3.jpg",
            "https://cdn.dummyjson.com/product-images/15/4.jpg",
            "https://cdn.dummyjson.com/product-images/15/thumbnail.jpg"
        ]
    }
]
