from airtable_integration import push_to_airtable

# test values
push_to_airtable(
    name="Test User",
    email="test@example.com",
    product="SUV",
    priority="Hot",
    generated_email="Hi Test, thanks for checking out our SUVs!"
)
