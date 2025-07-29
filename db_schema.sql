-- USERS
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    password_hash VARCHAR(255),
    role ENUM('admin', 'operator') NOT NULL
);

-- SUPPLIERS
CREATE TABLE suppliers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    contact VARCHAR(100)
);

-- CATEGORIES
CREATE TABLE categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100)
);

-- PRODUCTS
CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    barcode VARCHAR(100),
    sku_id VARCHAR(100),
    category_id INT,
    subcategory_id INT,
    price DECIMAL(10,2),
    gst DECIMAL(5,2),
    description TEXT,
    default_unit VARCHAR(50),
    conv_factor DECIMAL(5,2),
    image_path VARCHAR(255),
    supplier_id INT,
    FOREIGN KEY (category_id) REFERENCES categories(id),
    FOREIGN KEY (supplier_id) REFERENCES suppliers(id)
);

-- INVENTORY
CREATE TABLE inventory (
    product_id INT PRIMARY KEY,
    current_stock DECIMAL(10,2),
    FOREIGN KEY (product_id) REFERENCES products(id)
);
