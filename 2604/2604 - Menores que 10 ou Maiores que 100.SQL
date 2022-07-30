SELECT products.name, providers.name
FROM products, providers
WHERE id_categories = 6 and id_providers = providers.id
