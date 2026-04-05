from typing import List

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field


app = FastAPI(
    title="Tech Store Homepage API",
    description="Mock API for the homepage of a home appliances online store.",
    version="1.0.0",
)


# Enable CORS so the frontend can call the API from another origin.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Category(BaseModel):
    """Menu category shown on the homepage."""

    id: int = Field(..., description="Category identifier")
    name: str = Field(..., description="Category display name")


class Banner(BaseModel):
    """Hero banner item displayed on the homepage."""

    id: int = Field(..., description="Banner identifier")
    image_url: str = Field(..., description="Banner image URL")
    title: str = Field(..., description="Banner title")
    alt_text: str = Field(..., description="Alternative text for the image")


class Product(BaseModel):
    """Product card shown in homepage sections."""

    id: int = Field(..., description="Product identifier")
    name: str = Field(..., description="Product name")
    price: int = Field(..., description="Product price")
    currency: str = Field(..., description="Product currency")
    rating: int = Field(..., ge=0, le=5, description="Product rating")
    image_url: str = Field(..., description="Product image URL")


# In-memory mock database. This simulates a real database layer while the
# project is still under development.
MOCK_DB = {
    "categories": [
        {"id": 1, "name": "Телевизоры"},
        {"id": 2, "name": "Бытовая техника"},
        {"id": 3, "name": "Встраиваемая бытовая техника"},
        {"id": 4, "name": "Мелкая бытовая техника"},
    ],
    "banners": [
        {
            "id": 1,
            "image_url": "https://images.unsplash.com/photo-1585155770447-2f66e2a397b5?auto=format&fit=crop&w=1600&q=80",
            "title": "Весенние скидки на технику для дома",
            "alt_text": "Главный баннер интернет-магазина бытовой техники",
        }
    ],
    "deal_of_the_day": {
        "id": 101,
        "name": "Кондиционер Samsung AR09TXHQASINUA",
        "price": 51990,
        "currency": "сом",
        "rating": 5,
        "image_url": "https://images.unsplash.com/photo-1631049307264-da0ec9d70304?auto=format&fit=crop&w=800&q=80",
    },
    "new_products": [
        {
            "id": 201,
            "name": "Пылесос Tefal Bagless",
            "price": 20490,
            "currency": "сом",
            "rating": 4,
            "image_url": "https://images.unsplash.com/photo-1558317374-067fb5f30001?auto=format&fit=crop&w=800&q=80",
        },
        {
            "id": 202,
            "name": "Холодильник LG DoorCooling+",
            "price": 68990,
            "currency": "сом",
            "rating": 5,
            "image_url": "https://images.unsplash.com/photo-1584568694244-14fbdf83bd30?auto=format&fit=crop&w=800&q=80",
        },
        {
            "id": 203,
            "name": "Стиральная машина Bosch Serie 4",
            "price": 45990,
            "currency": "сом",
            "rating": 5,
            "image_url": "https://images.unsplash.com/photo-1626806787461-102c1bfaaea1?auto=format&fit=crop&w=800&q=80",
        },
        {
            "id": 204,
            "name": "Микроволновая печь Panasonic NN-ST34",
            "price": 12990,
            "currency": "сом",
            "rating": 4,
            "image_url": "https://images.unsplash.com/photo-1574269909862-7e1d70bb8078?auto=format&fit=crop&w=800&q=80",
        },
    ],
}


def fetch_categories() -> List[Category]:
    """Returns categories from the mock database."""

    return [Category(**item) for item in MOCK_DB["categories"]]


def fetch_banners() -> List[Banner]:
    """Returns banners from the mock database."""

    return [Banner(**item) for item in MOCK_DB["banners"]]


def fetch_deal_of_the_day() -> Product:
    """Returns the product of the day from the mock database."""

    return Product(**MOCK_DB["deal_of_the_day"])


def fetch_new_products() -> List[Product]:
    """Returns new products from the mock database."""

    return [Product(**item) for item in MOCK_DB["new_products"]]


@app.get("/", response_class=HTMLResponse)
def homepage() -> str:
    """Returns a simple frontend page connected to the API."""

    return """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Tech Store</title>
        <style>
            :root {
                --bg: #f5f7fb;
                --surface: #ffffff;
                --text: #18202f;
                --muted: #6d7788;
                --accent: #ff6b2c;
                --accent-dark: #dc4f18;
                --line: #dfe5ef;
                --shadow: 0 18px 45px rgba(24, 32, 47, 0.08);
            }

            * {
                box-sizing: border-box;
            }

            body {
                margin: 0;
                font-family: "Segoe UI", Tahoma, sans-serif;
                background:
                    radial-gradient(circle at top left, #fff3eb 0, transparent 30%),
                    linear-gradient(180deg, #f9fbff 0%, #eef3f9 100%);
                color: var(--text);
            }

            .container {
                width: min(1180px, calc(100% - 32px));
                margin: 0 auto;
            }

            header {
                padding: 24px 0 12px;
            }

            .topbar {
                display: flex;
                justify-content: space-between;
                align-items: center;
                gap: 16px;
                flex-wrap: wrap;
            }

            .brand {
                font-size: 32px;
                font-weight: 800;
                letter-spacing: 0.04em;
            }

            .brand span {
                color: var(--accent);
            }

            .subtitle {
                color: var(--muted);
                margin-top: 6px;
            }

            .menu {
                display: flex;
                flex-wrap: wrap;
                gap: 10px;
                margin: 24px 0 8px;
            }

            .menu-item {
                padding: 10px 16px;
                border-radius: 999px;
                background: rgba(255, 255, 255, 0.8);
                border: 1px solid var(--line);
                box-shadow: 0 4px 16px rgba(24, 32, 47, 0.04);
                font-size: 14px;
            }

            .hero {
                margin: 28px 0;
                background: var(--surface);
                border-radius: 28px;
                overflow: hidden;
                box-shadow: var(--shadow);
                display: grid;
                grid-template-columns: 1.1fr 0.9fr;
                min-height: 320px;
            }

            .hero-copy {
                padding: 42px;
                display: flex;
                flex-direction: column;
                justify-content: center;
            }

            .eyebrow {
                color: var(--accent);
                font-size: 14px;
                font-weight: 700;
                text-transform: uppercase;
                letter-spacing: 0.08em;
                margin-bottom: 12px;
            }

            .hero h1 {
                margin: 0;
                font-size: clamp(32px, 4vw, 54px);
                line-height: 1.02;
            }

            .hero p {
                margin: 16px 0 0;
                color: var(--muted);
                font-size: 18px;
                line-height: 1.6;
            }

            .hero-image {
                min-height: 320px;
                background-size: cover;
                background-position: center;
            }

            .section-title {
                font-size: 28px;
                margin: 28px 0 18px;
            }

            .deal-card,
            .product-card {
                background: var(--surface);
                border-radius: 24px;
                box-shadow: var(--shadow);
                overflow: hidden;
            }

            .deal-card {
                display: grid;
                grid-template-columns: 340px 1fr;
                margin-bottom: 28px;
            }

            .deal-image,
            .product-image {
                background-size: cover;
                background-position: center;
                min-height: 240px;
            }

            .deal-body {
                padding: 28px;
            }

            .price {
                font-size: 30px;
                font-weight: 800;
                margin: 10px 0;
            }

            .rating {
                color: #f6a300;
                font-size: 18px;
                letter-spacing: 0.08em;
            }

            .products-grid {
                display: grid;
                grid-template-columns: repeat(4, minmax(0, 1fr));
                gap: 18px;
                margin-bottom: 40px;
            }

            .product-card {
                display: flex;
                flex-direction: column;
            }

            .product-body {
                padding: 20px;
            }

            .product-name {
                font-size: 18px;
                font-weight: 700;
                margin: 0 0 10px;
                min-height: 48px;
            }

            .muted {
                color: var(--muted);
            }

            footer {
                color: var(--muted);
                padding: 0 0 40px;
                text-align: center;
            }

            @media (max-width: 980px) {
                .hero,
                .deal-card,
                .products-grid {
                    grid-template-columns: 1fr;
                }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <header>
                <div class="topbar">
                    <div>
                        <div class="brand">TECH<span>STORE</span></div>
                        <div class="subtitle">Главная страница, подключенная к FastAPI</div>
                    </div>
                </div>
                <nav class="menu" id="categories"></nav>
            </header>

            <main>
                <section class="hero">
                    <div class="hero-copy">
                        <div class="eyebrow">Интернет-магазин техники</div>
                        <h1 id="banner-title">Загрузка баннера...</h1>
                        <p>Выбирайте бытовую технику для дома с доставкой, гарантией и выгодными предложениями каждый день.</p>
                    </div>
                    <div class="hero-image" id="banner-image"></div>
                </section>

                <h2 class="section-title">Товар дня</h2>
                <section class="deal-card">
                    <div class="deal-image" id="deal-image"></div>
                    <div class="deal-body">
                        <div class="muted">Специальное предложение</div>
                        <h3 id="deal-name">Загрузка...</h3>
                        <div class="price" id="deal-price"></div>
                        <div class="rating" id="deal-rating"></div>
                    </div>
                </section>

                <h2 class="section-title">Новинки</h2>
                <section class="products-grid" id="new-products"></section>
            </main>

            <footer>Mock frontend + mock database inside one FastAPI app.</footer>
        </div>

        <script>
            function renderStars(rating) {
                return "★".repeat(rating) + "☆".repeat(5 - rating);
            }

            async function fetchJson(url) {
                const response = await fetch(url);
                if (!response.ok) {
                    throw new Error("Request failed: " + response.status);
                }
                return response.json();
            }

            async function loadHomepage() {
                const [categories, banners, dealOfTheDay, newProducts] = await Promise.all([
                    fetchJson("/api/categories"),
                    fetchJson("/api/banners"),
                    fetchJson("/api/products/deal-of-the-day"),
                    fetchJson("/api/products/new")
                ]);

                document.getElementById("categories").innerHTML = categories
                    .map((category) => `<div class="menu-item">${category.name}</div>`)
                    .join("");

                const banner = banners[0];
                document.getElementById("banner-title").textContent = banner.title;
                document.getElementById("banner-image").style.backgroundImage =
                    `url("${banner.image_url}")`;

                document.getElementById("deal-name").textContent = dealOfTheDay.name;
                document.getElementById("deal-price").textContent =
                    `${dealOfTheDay.price} ${dealOfTheDay.currency}`;
                document.getElementById("deal-rating").textContent =
                    renderStars(dealOfTheDay.rating);
                document.getElementById("deal-image").style.backgroundImage =
                    `url("${dealOfTheDay.image_url}")`;

                document.getElementById("new-products").innerHTML = newProducts
                    .map((product) => `
                        <article class="product-card">
                            <div
                                class="product-image"
                                style="background-image: url('${product.image_url}')"
                            ></div>
                            <div class="product-body">
                                <h3 class="product-name">${product.name}</h3>
                                <div class="price">${product.price} ${product.currency}</div>
                                <div class="rating">${renderStars(product.rating)}</div>
                            </div>
                        </article>
                    `)
                    .join("");
            }

            loadHomepage().catch((error) => {
                console.error(error);
                document.body.insertAdjacentHTML(
                    "beforeend",
                    '<p style="text-align:center;color:#b42318;">Не удалось загрузить данные с API.</p>'
                );
            });
        </script>
    </body>
    </html>
    """


@app.get("/api/categories", response_model=List[Category])
def get_categories() -> List[Category]:
    """Returns the homepage menu categories."""

    return fetch_categories()


@app.get("/api/banners", response_model=List[Banner])
def get_banners() -> List[Banner]:
    """Returns hero banner data."""

    return fetch_banners()


@app.get("/api/products/deal-of-the-day", response_model=Product)
def get_deal_of_the_day() -> Product:
    """Returns the deal of the day product."""

    return fetch_deal_of_the_day()


@app.get("/api/products/new", response_model=List[Product])
def get_new_products() -> List[Product]:
    """Returns a list of new products."""

    return fetch_new_products()
