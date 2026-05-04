# Theming

After your development environment is fully set up, you can start building the skeleton of your theme module. In this chapter, you will discover how to:

- Enable/disable the Website Builder’s standard options and templates.
- Define the colors and fonts to use for your design.
- Get the most out of Bootstrap variables.
- Add custom styles and JavaScript.

## Theme module

Odoo comes with a default theme that provides minimal structure and layout. When you create a new theme, you are extending the default theme.

Remember to add the directory containing your module to the `addons-path` command-line argument when running Odoo in your development environment.

### Technical naming

The first step is to create a new directory.

```xml
website_airproof
```

> **Note**: Prefix it with `website_` and use only lowercase ASCII alphanumeric characters and underscores.
> 
> In this documentation, we will use **Airproof** (a fictional project) as an example.

### File structure

Themes are packaged like any Odoo module. Even if you are designing a basic website, you need to package its theme like a module.

```text
website_airproof
├── data
├── i18n
├── static
│   ├── description
│   ├── fonts
│   ├── lib
│   ├── image_shapes // Shapes for images
│   ├── shapes // Shapes for background
│   └── src
│       ├── img
│       │   ├── content // For those used in the pages of your website
│       │   └── wbuilder // For those used in the builder
│       ├── js
│       ├── scss // Theme specific styles
│       ├── snippets // Custom snippets
│       └── website_builder // Options for the Website Builder
├── views
├── __init__.py
└── __manifest__.py
```

| Folder | Description |
| :--- | :--- |
| **data** | Presets, menus, pages, images, shapes, … (`*.xml`) |
| **i18n** | Translations (`*.po`, `*.pot`) |
| **lib** | External libraries (`*.js`) |
| **static** | Custom assets (`*.jpg`, `*.gif`, `*.png`, `*.svg`, `*.pdf`, `*.scss`, `*.js`) |
| **views** | Custom views and templates (`*.xml`) |

### Initialization

An Odoo module is also a Python package with a `__init__.py` file containing import instructions for various Python files in the module. This file can remain empty for now.

### Declaration

An Odoo module is declared by its manifest file. This file declares a Python package as an Odoo module and specifies the module’s metadata. It must at least contain the `name` field, which is always required.

> `/website_airproof/__manifest__.py`
> ```python
> {
>    'name': 'Airproof Theme',
>    'description': '...',
>    'category': 'Website/Theme',
>    'version': '19.0.0',
>    'author': '...',
>    'license': '...',
>    'depends': ['website'],
>    'data': [
>       # ...
>    ],
>    'assets': {
>       # ...
>    },
> }
> ```

| Field | Description |
| :--- | :--- |
| **name** | Human-readable name of the module (required) |
| **description** | Extended description of the module, in reStructuredText |
| **category** | Classification category within Odoo |
| **version** | Odoo version this module is addressing |
| **author** | Name of the module author |
| **license** | By default, we use the `LGPL-3` license. |
| **depends** | Odoo modules must be loaded before this one. |
| **data** | List of XML files |
| **assets** | List of SCSS and JS files |

> **Note**:
> - To create a website theme, you only need to install the Website app.
> - Odoo version and major number are mandatory. Odoo versioning follows `odoo_major.odoo_minor.module_major.module_minor.module_patch`. Example: `19.0.1.0.0`

> **Warning**: Automated file inclusion using wildcard notations (ex.: `/myfolder/*.scss`) doesn’t work in Odoo SaaS databases. In this case, include each file manually in the manifest.

## Default options

### Odoo variables

Odoo declares many CSS rules customizable by overriding the related SCSS variables. To do so, create a `primary_variables.scss` file and add it to the `_assets_primary_variables` bundle.

**Declaration**

> `/website_airproof/__manifest__.py`
> ```python
> 'assets': {
>    'web._assets_primary_variables': [
>       'website_airproof/static/src/scss/primary_variables.scss',
>    ],
> },
> ```

#### Global

**Declaration**

> `/website_airproof/static/src/scss/primary_variables.scss`
> ```scss
> $o-website-values-palettes: (
>    (
>       // Templates, Colors, Fonts, Buttons, etc.
>    ),
> );
> ```

#### Fonts

You can embed any font on your website. The Website Builder automatically makes them available in the font selector.

**Declaration**

> `/website_airproof/static/src/scss/primary_variables.scss`
> ```scss
> $o-theme-font-configs: (
>    <font-name>: (
>       'family': <CSS font family list>,
>       'url' (optional): <related part of Google fonts URL>,
>       'properties' (optional): (
>          <font-alias>: (
>             <website-value-key>: <value>,
>             ...,
>          ),
>       ...,
>    )
> )
> ```

**Use**

> `/website_airproof/static/src/scss/primary_variables.scss`
> ```scss
> $o-website-values-palettes: (
>    (
>       'font':                             '<font-name>',
>       'headings-font':                    '<font-name>',
>       'navbar-font':                      '<font-name>',
>       'buttons-font':                     '<font-name>',
>    ),
> );
> ```

##### Google fonts

> `/website_airproof/static/src/scss/primary_variables.scss`
> ```scss
> $o-theme-font-configs: (
>    'Poppins': (
>       'family':                         ('Poppins', sans-serif),
>       'url':                            'Poppins:400,500',
>       'properties' : (
>          'base': (
>             'font-size-base':           1rem,
>          ),
>       ),
>    ),
> );
> ```

##### Custom fonts

First, create a specific SCSS file to declare your custom font(s) and add it to `web.assets_frontend`.

> `/website_airproof/static/src/scss/fonts.scss`
> ```scss
> @font-face {
>    font-family: "My Custom Font", Helvetica, Helvetica Neue, Arial, sans-serif;
>    font-weight: 400;
>    font-style: normal;
>    src: url('/fonts/my-custom-font.woff') format('woff'),
>         url('/fonts/my-custom-font.woff2') format('woff2');
> }
> ```

Then register it in `primary_variables.scss`:

> `/website_airproof/static/src/scss/primary_variables.scss`
> ```scss
> $o-theme-font-configs: (
>    'Proxima Nova': (
>       'family':                         ('Proxima Nova', sans-serif),
>       'properties' : (
>          'base': (
>             'font-size-base':           1rem,
>          ),
>       ),
>    ),
> );
> ```

#### Colors

The Website Builder relies on palettes composed of five named colors.

| Color | Description |
| :--- | :--- |
| **o-color-1** | Primary |
| **o-color-2** | Secondary |
| **o-color-3** | Extra (Light) |
| **o-color-4** | Whitish |
| **o-color-5** | Blackish |

**Declaration**

> `/website_airproof/static/src/scss/primary_variables.scss`
> ```scss
> $o-color-palettes: map-merge($o-color-palettes,
>    (
>       'airproof': (
>          'o-color-1':                    #bedb39,
>          'o-color-2':                    #2c3e50,
>          'o-color-3':                    #f2f2f2,
>          'o-color-4':                    #ffffff,
>          'o-color-5':                    #000000,
>       ),
>    )
> );
>
> $o-selected-color-palettes-names: append($o-selected-color-palettes-names, 'airproof');
> ```

**Use**

```scss
$o-website-values-palettes: (
   (
      'color-palettes-name':              'airproof',
   ),
);
```

**Color combinations**

Odoo generates five color combinations (`o-cc1` to `o-cc5`). You can override them in `$o-color-palettes` using the `o-cc*` prefix.

> `/website_airproof/static/src/scss/primary_variables.scss`
> ```scss
> $o-color-palettes: map-merge($o-color-palettes,
>    (
>       'airproof': (
>          'o-cc1-bg':                     'o-color-1',
>          'o-cc1-text':                   'o-color-5',
>          'o-cc1-headings':               'o-color-5',
>          'o-cc1-link':                   'o-color-2',
>          'o-cc1-btn-primary':            'o-color-2',
>          // ...
>       ),
>    )
> );
> ```

#### Gradients

Define gradients for the menu, header, footer and copyright bar.

> `/website_airproof/static/src/scss/primary_variables.scss`
> ```scss
> $o-website-values-palettes: (
>    (
>       'menu-gradient': linear-gradient(135deg, rgb(203, 94, 238) 0%, rgb(75, 225, 236) 100%),
>       'header-boxed-gradient': [your-gradient],
>       'footer-gradient': [your-gradient],
>       'copyright-gradient': [your-gradient],
>    ),
> );
> ```

### Bootstrap variables

Use a dedicated file added to the `web._assets_frontend_helpers` bundle to override Bootstrap values.

**Declaration**

> `/website_airproof/__manifest__.py`
> ```python
> 'assets': {
>    'web._assets_frontend_helpers': [
>       ('prepend', 'website_airproof/static/src/scss/bootstrap_overridden.scss'),
>    ],
> },
> ```

**Use**

> `/website_airproof/static/src/scss/bootstrap_overridden.scss`
> ```scss
> // Typography
> $h1-font-size:                 4rem !default;
>
> // Navbar
> $navbar-nav-link-padding-x:    1rem !default;
>
> // Buttons + Forms
> $input-placeholder-color:      o-color('o-color-1') !default;
>
> // Cards
> $card-border-width:            0 !default;
> ```

#### Font sizes

##### Text style

Odoo uses Bootstrap classes for text styling:
- `display-1` to `display-4` for large titles.
- `lead` for introduction text.
- `o_small` for body text with a smaller size.

##### Sizing classes

Sizing classes are added on a `span` tag inside the element:
- `h1-fs` to `h6-fs`
- `base-fs` (16px by default)
- `o_small-fs` (14px by default)
- `display-1-fs` to `display-4-fs`

## Website settings

Global options related to the website can be set through the website record.

**Declaration**

> `/website_airproof/data/website.xml`
> ```xml
> <?xml version="1.0" encoding="utf-8"?>
> <odoo noupdate="1">
>    <record id="website.default_website" model="website">
>       <field name="name">Airproof</field>
>       <field name="logo" type="base64" file="website_airproof/static/src/img/content/logo_airproof.png"/>
>       <field name="favicon" type="base64" file="website_airproof/static/description/favicon.png" />
>       <field name="shop_ppg">18</field>
>       <field name="shop_ppr">3</field>
>       <field name="shop_gap">16px</field>
>       <field name="shop_opt_products_design_classes">
>             o_wsale_products_opt_layout_catalog
>             o_wsale_products_opt_design_cards
>             ...
>       </field>
>       <field name="cookies_bar" eval="True" />
>       <field name="social_facebook">https://www.facebook.com/Airproof</field>
>       <!-- ... -->
>    </record>
> </odoo>
> ```

## Views

### Presets

Activate and deactivate views in `presets.xml`.

> `/website_airproof/data/presets.xml`
> ```xml
> <record id="website.template_header_default_align_center" model="ir.ui.view">
>    <field name="active" eval="True"/>
> </record>
>
> <record id="portal.footer_language_selector" model="ir.ui.view">
>    <field name="active" eval="False" />
> </record>
> ```

## Assets

| Bundle | Description |
| :--- | :--- |
| **web._assets_primary_variables** | For `primary_variables.scss`. |
| **web._assets_frontend_helpers** | For `bootstrap_overridden.scss`. |
| **web.assets_frontend** | For theme SCSS, JS, and external libraries. |
| **website.website_builder_assets** | For JS related to Website Builder options. |

### Styles

Add any SCSS file to the `web.assets_frontend` bundle.

> `/website_airproof/static/src/scss/theme.scss`
> ```scss
> blockquote {
>    border-radius: $rounded-pill;
>    color: o-color('o-color-3');
>    font-family: o-website-value('headings-font');
> }
> ```

### Interactivity

Most new Odoo JavaScript code should use the **native JavaScript module system**.

**Declaration**

> `/website_airproof/__manifest__.py`
> ```python
> 'assets': {
>    'web.assets_frontend': [
>       'website_airproof/static/src/js/theme.js',
>    ],
> },
> ```

**Best Practices**

- Use a linter (ESLint).
- Use `js_` prefixed CSS classes for targeting elements.
- Variables and functions: `camelCase`.
- Classes: `PascalCase`.
- Use `ev` instead of `event`.
- Use strict comparisons (`===`).
- Use double quotes for strings.
- Call `super` when overriding standard functions.
