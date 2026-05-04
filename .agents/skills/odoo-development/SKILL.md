---
name: odoo-development
description: Odoo 19 development standards for building and customizing this personal and freelancing website. Use for Python coding, QWeb/XML templating, and layout decisions aligned with the project's design and documentation.
---

# Odoo Development - Personal & Freelancing Website

This skill ensures consistency and adherence to Odoo 19 best practices specifically for this personal/freelancing project's visual and functional requirements.

## Development Standards

### Python Naming
- Use `snake_case` for all Python names, including variables, functions, and classes (where applicable by Odoo standards).
- Ensure keys passed to QWeb templates are also in `snake_case`.

### Odoo 19 Best Practices
- Follow official Odoo 19 guidelines for:
    - **Architecture**: Proper module structure and dependency management.
    - **ORM**: Efficient database interactions using Odoo's ORM.
    - **Security**: Implementation of access rights and record rules.
    - **QWeb/XML**: Clean and maintainable template patterns.
    - **Testing**: Comprehensive unit and integration tests.

### Design Language
- Treat `DESIGN.md` as the canonical design language document for the website.
- Use it to guide all visual, layout, typography, and component decisions.
- Do not deviate from `DESIGN.md` unless explicitly overridden by the user.

## Documentation & Reference

For detailed guidance on Odoo 19 website building and customization, refer to the local documentation in the `@docs/` folder:
- `Odoo19_Layout.md`: Headers, footers, XPaths, and responsive design.
- `Odoo19_Navigation.md`: Menu items, dropdowns, and mega menus.
- `Odoo19_Pages.md`: Static pages, page records, and templates.
- `Odoo19_Theming.md`: Module structure, assets, colors, and fonts.
