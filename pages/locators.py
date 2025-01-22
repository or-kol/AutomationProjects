from selenium.webdriver.common.by import By

class Locators:
    # ============================
    # Common Locators (used across multiple pages)
    # ============================
    CART_BTN = (By.CSS_SELECTOR, "#shopping_cart_container")
    ERROR_MSG = (By.CSS_SELECTOR, ".error-message-container")
    CANCEL_BTN = (By.CSS_SELECTOR, "#cancel")

    # Remove from Cart buttons for Products List Page and Cart Page
    SAUCE_LABS_BACKPACK_REMOVE_FROM_CART_BTN = (By.CSS_SELECTOR, "#remove-sauce-labs-backpack")
    SAUCE_LABS_BIKE_LIGHT_REMOVE_FROM_CART_BTN = (By.CSS_SELECTOR, "#remove-sauce-labs-bike-light")
    SAUCE_LABS_BOLT_TSHIRT_REMOVE_FROM_CART_BTN = (By.CSS_SELECTOR, "#remove-sauce-labs-bolt-t-shirt")
    SAUCE_LABS_FLEECE_JACKET_REMOVE_FROM_CART_BTN = (By.CSS_SELECTOR, "#remove-sauce-labs-fleece-jacket")
    SAUCE_LABS_ONESIE_REMOVE_FROM_CART_BTN = (By.CSS_SELECTOR, "#remove-sauce-labs-onesie")
    TEST_ALL_THE_THINGS_REMOVE_FROM_CART_BTN = (By.CSS_SELECTOR, "[id^='remove-test']")

    # ============================
    # Login Page Locators
    # ============================
    USER_NAME_FIELD = (By.CSS_SELECTOR, "#user-name")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#password")
    LOGIN_BTN = (By.CSS_SELECTOR, "#login-button")

    # ============================
    # Products List Page Locators
    # ============================
    SAUCE_LABS_BACKPACK_BTN = (By.CSS_SELECTOR, "#item_4_title_link")
    SAUCE_LABS_BIKE_LIGHT_BTN = (By.CSS_SELECTOR, "#item_0_title_link")
    SAUCE_LABS_BOLT_TSHIRT_BTN = (By.CSS_SELECTOR, "#item_1_title_link")
    SAUCE_LABS_FLEECE_JACKET_BTN = (By.CSS_SELECTOR, "#item_5_title_link")
    SAUCE_LABS_ONESIE_BTN = (By.CSS_SELECTOR, "#item_2_title_link")
    TEST_ALL_THE_THINGS_BTN = (By.CSS_SELECTOR, "#item_3_title_link")
    PRODUCT_LIST_PAGE_TITLE = (By.CSS_SELECTOR, ".title")

    PRODUCTS_NAMES_LIST = (By.CSS_SELECTOR,
                           ".inventory_list>.inventory_item>.inventory_item_description>.inventory_item_label>[data-test$='title-link']>.inventory_item_name")
    PRODUCTS_PRICES_LIST = (By.CSS_SELECTOR,
                            ".inventory_list>.inventory_item>div.inventory_item_description>div.pricebar>div")

    # Add to Cart buttons for Products List Page
    SAUCE_LABS_BACKPACK_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
    SAUCE_LABS_BIKE_LIGHT_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bike-light")
    SAUCE_LABS_BOLT_TSHIRT_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")
    SAUCE_LABS_FLEECE_JACKET_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-fleece-jacket")
    SAUCE_LABS_ONESIE_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")
    TEST_ALL_THE_THINGS_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id^='add-to-cart-test']")

    # Sorting dropdown for Products List Page
    PRODUCT_SORT = (By.CSS_SELECTOR, ".product_sort_container")

    # ============================
    # Cart Page Locators
    # ============================
    CONTINUE_SHOPPING_BTN = (By.CSS_SELECTOR, "#continue-shopping")
    CHECKOUT_BTN = (By.CSS_SELECTOR, "#checkout")
    CART_LIST = (By.CSS_SELECTOR, ".cart_list>[data-test='inventory-item']")
    CART_PAGE_TITLE = (By.CSS_SELECTOR, ".title")

    # ============================
    # Checkout Page Locators
    # ============================
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, "#first-name")
    LAST_NAME_FIELD = (By.CSS_SELECTOR, "#last-name")
    ZIP_CODE_FIELD = (By.CSS_SELECTOR, "#postal-code")
    CONTINUE_BTN = (By.CSS_SELECTOR, "#continue")
    CHECKOUT_PAGE_TITLE = (By.CSS_SELECTOR, ".title")

    # ============================
    # Complete Purchase Page Locators
    # ============================
    BACK_HOME_BTN = (By.CSS_SELECTOR, "#back-to-products")
    COMPLETE_MSG = (By.CSS_SELECTOR, ".complete-header")

    # ============================
    # Overview Page Locators
    # ============================
    FINISH_BTN = (By.CSS_SELECTOR, "#finish")
    OVERVIEW_PAGE_TITLE = (By.CSS_SELECTOR, ".title")
    PAYMENT_INFO = (By.CSS_SELECTOR, "[data-test='payment-info-value']")
    SHIPPING_INFO = (By.CSS_SELECTOR, "[data-test='shipping-info-value']")
    ITEM_PRICE_INFO = (By.CSS_SELECTOR, ".summary_subtotal_label")
    TAX_INFO = (By.CSS_SELECTOR, ".summary_tax_label")
    TOTAL_PRICE_INFO = (By.CSS_SELECTOR, ".summary_total_label")

    # ============================
    # Product Page Locators
    # ============================
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "#add-to-cart")
    REMOVE_FROM_CART_BTN = (By.CSS_SELECTOR, "#remove")
    BACK_TO_PRODUCTS_LIST_PAGE_BTN = (By.CSS_SELECTOR, "#back-to-products")
    PRODUCTS_NAME = (By.CSS_SELECTOR, ".inventory_details_name")

