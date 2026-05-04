# Layout

In this chapter, you will learn how to:

- Create a custom header.
- Create a custom footer.
- Modify a standard template.
- Add a copyright section.
- Improve your website’s responsiveness.

## Default

An Odoo page combines cross-page and unique elements. Cross-page elements are the same on every page, while unique elements are only related to a specific page. By default, a page has two cross-page elements, the header and the footer, and a unique main element that contains the specific content of that page.

```xml
<div id="wrapwrap">
   <header/>
      <main>
         <div id="wrap" class="oe_structure">
            <!-- Page Content -->
         </div>
      </main>
   <footer/>
</div>
```

Any Odoo XML file starts with encoding specifications. After that, you must write your code inside an `<odoo>` tag.

```xml
<?xml version="1.0" encoding="utf-8" ?>
<odoo>
   ...
</odoo>
```

> **Note**: Using precise template names is important to find information through all modules quickly. Template names should only contain lowercase alphanumerics and underscores.
>
> Always add an empty line at the end of your file. This can be done automatically by configuring your IDE.

## XPath

XPath (XML Path Language) is an expression language that enables you to navigate through elements and attributes in an XML document easily. XPath is used to extend standard Odoo templates.

A view is coded the following way:

```xml
<template id="..." inherit_id="..." name="...">
   <!-- Content -->
</template>
```

| Attribute | Description |
| :--- | :--- |
| **id** | ID of the modified view |
| **inherited_id** | ID of the standard view (using the following pattern: `module.template`) |
| **name** | Human-readable name of the modified view |

For each XPath, you modify two attributes: **expression** and **position**.

> **Example**: `/website_airproof/views/website_templates.xml`
> ```xml
> <template id="layout" inherit_id="website.layout" name="Welcome Message">
>    <xpath expr="//header" position="before">
>       <!-- Content -->
> </xpath>
> </template>
> ```
> This XPath adds a welcome message right before the page content.

> **Warning**: Be careful when replacing default elements’ attributes. As your theme extends the default one, your changes will take priority over any future Odoo update.

> **Note**:
> - You should update your module every time you create a new template or record.
> - *XML IDs* of inheriting views should use the same *ID* as the original record. It helps to find all inheritance at a glance. As final *XML IDs* are prefixed by the module that creates them, there is no overlap.

### Expressions

XPath uses path expressions to select nodes in an XML document. Selectors are used inside the expression to target the right element. The most useful ones are listed below.

| Descendent selectors | Description |
| :--- | :--- |
| **/** | Selects from the root node. |
| **//** | Selects nodes in the document from the current node that matches the selection no matter where they are. |

| Attribute selectors | Description |
| :--- | :--- |
| **\*** | Selects any XML tag. `*` can be replaced by a specific tag if the selection needs to be more precise. |
| **\*[@id=”id”]** | Selects a specific ID. |
| **\*[hasclass(“class”)]** | Selects a specific class. |
| **\*[@name=”name”]** | Selects a tag with a specific name. |
| **\*[@t-call=”t-call”]** | Selects a specific t-call. |

### Position

The position defines where the code is placed inside the template. The possible values are listed below:

| Position | Description |
| :--- | :--- |
| **replace** | Replaces the targeted node with the XPath content. |
| **inside** | Adds the XPath content inside the targeted node. |
| **before** | Adds the XPath content before the targeted node. |
| **after** | Adds the XPath content after the targeted node. |
| **attributes** | Adds the XPath content inside an attribute. |

> **Example**:
> 
> This XPath removes the first element with a `.breadcrumb` class.
> ```xml
> <xpath expr="//*[hasclass('breadcrumb')]" position="replace"/>
> ```
> 
> This XPath adds an extra `<li>` element after the last child of the `<ul>` element.
> ```xml
> <xpath expr="//ul" position="inside">
>    <li>Last element of the list</li>
> </xpath>
> ```
> 
> This XPath adds a `<div>` before the `<nav>` that is a direct child of the `<header>`.
> ```xml
> <xpath expr="//header/nav" position="before">
>    <div>Some content before the header</div>
> </xpath>
> ```
> 
> This XPath removes `x_airproof_header` in the class attribute of the header. In this case, you don’t need to use the `separator` attribute.
> ```xml
> <xpath expr="//header" position="attributes">
>    <attribute name="class" remove="x_airproof_header" />
> </xpath>
> ```
> 
> This XPath adds `x_airproof_header` in the class attribute of the header. You also need to define a `separator` attribute to add a space before the class you are adding.
> ```xml
> <xpath expr="//header" position="attributes">
>    <attribute name="class" add="x_airproof_header" separator=" " />
> </xpath>
> ```
> 
> This XPath moves the element with `.o_footer_scrolltop_wrapper` class before the element with the `footer` ID attribute.
> ```xml
> <xpath expr="//div[@id='footer']" position="before">
>    <xpath expr="//div[@id='o_footer_scrolltop_wrapper']" position="move" />
> </xpath>
> ```

> **Tip**: Using `move` directives inside another XPath forces you to use only this kind of directive.
> 
> **Good example:**
> ```xml
> <xpath expr="//*[hasclass('o_wsale_products_main_row')]" position="before">
>    <xpath expr="//t[@t-if='opt_wsale_categories_top']" position="move" />
> </xpath>
> <xpath expr="//*[hasclass('o_wsale_products_main_row')]" position="before">
>    <div><!-- Content --></div>
> </xpath>
> ```
> 
> **Bad example:**
> ```xml
> <xpath expr="//*[hasclass('o_wsale_products_main_row')]" position="before">
>    <xpath expr="//t[@t-if='opt_wsale_categories_top']" position="move" />
>    <div><!-- Content --></div>
> </xpath>
> ```

## QWeb

QWeb is the primary templating engine used by Odoo. It is an XML templating engine mainly used to generate HTML fragments and pages.

`t-call` directives can receive parameters:

```xml
<!-- Old way -->
<t t-call="portal.user_dropdown">
   <t t-set="_icon" t-value="True" />
   <t t-set="_item_class" t-valuef="dropdown" />
</t>

<t t-call="website.layout">
   <t t-set="additional_title">My page title</t>
</t>

<!-- New way (Parametric) -->
<t t-call="portal.user_dropdown"
   _icon="true"
   _item_class.f="dropdown" />

<t t-call="website.layout"
   additional_title.translate="My page title" />
```

| Attribute (examples) | Description |
| :--- | :--- |
| `_icon="true"` | Pass the raw value (here a boolean set to `true`) |
| `_item_class.f="dropdown"` | Pass value as a string |
| `additional_title.translate="My page title"` | Pass value as a string |

## Custom fields

Depending on your needs, you can create custom fields to save data in the database.

### Declaration

First, create a record to declare the field. This field has to be linked to an existing model.

> `/website_airproof/data/fields.xml`
> ```xml
> <record id="x_post_category" model="ir.model.fields">
>    <field name="name">x_post_category</field>
>    <field name="field_description">...</field>
>    <field name="ttype">html</field>
>    <field name="state">manual</field>
>    <field name="index">0</field>
>    <field name="model_id" ref="website_blog.model_blog_post" />
> </record>
> ```

> **Note**: Fields creation is also possible (and recommended) through a model using Python.

### Back-end

Add the field to the relevant view through an XPath. Therefore, the user can see the field in the interface and fill it afterwards.

> `/website_airproof/views/backend/website_blog_views.xml`
> ```xml
> <record id="view_blog_post_form_category" model="ir.ui.view">
>    <field name="name">view_blog_post_form_category</field>
>    <field name="model">blog.post</field>
>    <field name="inherit_id" ref="website_blog.view_blog_post_form" />
>    <field name="arch" type="xml">
>       <xpath expr="//field[@name='blog_id']" position="before">
>          <field name="x_post_category" string="..." placeholder="..." />
>       </xpath>
>    </field>
> </record>
> ```

### Front-end

The field value can be shown somewhere in a page by calling `model_name.field_name` like this:

> `/website_airproof/views/website_blog_templates.xml`
> ```xml
> <h1 t-field="blog_post.x_post_category" />
> ```

## Background

You can define a color or an image as the background of your website.

### Colors

> `/website_airproof/static/src/scss/primary_variables.scss`
> ```scss
> $o-color-palettes: map-merge($o-color-palettes,
>    (
>       'airproof': (
>          'o-cc1-bg':                     'o-color-5',
>          'o-cc5-bg':                     'o-color-1',
>       ),
>     )
> );
> ```

### Image/pattern

> `/website_airproof/static/src/scss/primary_variables.scss`
> ```scss
> $o-website-values-palettes: (
>    (
>       'body-image': '/website_airproof/static/src/img/background-lines.svg',
>       'body-image-type': 'image' or 'pattern'
>    )
> );
> ```

## Header

By default, the header contains two distinct templates (desktop and mobile) which display the main navigation, the company’s logo and other optional elements (call-to-action, language selector, etc). Depending on the situation, choose between enabling/disabling existing elements with a standard template or building a brand new custom template.

### Standard

The Odoo Website Builder distinguishes between desktop templates and the mobile template in order to facilitate the adaptation of the user experience according to the device.

#### Desktop template

Enable one of the header default templates.

> **Important**: Don’t forget that you may need to disable the active header template first.
> 
> **Example**: `/website_aiproof/data/presets.xml`
> ```xml
> <record id="website.template_header_default" model="ir.ui.view">
>    <field name="active" eval="False" />
> </record>
> ```

Explicitly set the desired template in the `primary_variables.scss` file.

> `/website_airproof/static/src/scss/primary_variables.scss`
> ```scss
> $o-website-values-palettes: (
>    (
>       'header-template': 'stretch',
>    ),
> );
> ```

> `/website_airproof/data/presets.xml`
> ```xml
> <record id="website.template_header_stretch" model="ir.ui.view">
>    <field name="active" eval="True" />
> </record>
> ```

#### Mobile template

Each header template comes with the `template_header_mobile` template ensuring a seamless user experience across every device.

### Custom

Create your own template and add it to the list.

> **Important**: Don’t forget that you may need to disable the active header template first before enabling the custom one.

**Option**

Use the following code to add an option for your new custom header on the Website Builder.

> `/website_airproof/static/src/website_builder/header_template_option.xml`
> ```xml
> <t t-name="website_airproof.HeaderTemplateOption" t-inherit="website.HeaderTemplateOption" t-inherit-mode="extension">
>    <xpath expr="//BuilderRow[@label.translate='Template']//BuilderSelect" position="inside">
>       <BuilderSelectItem
>          id="'header_airproof_opt'"
>          title.translate="Airproof"
>          actionParam="[
>             {
>                action: 'websiteConfig',
>                actionParam: {
>                   views: ['website_airproof.header'],
>                   vars: { 'header-template': 'airproof' },
>                   checkVars: false,
>                },
>             },
>          ]">
>          <Img src="'/website_airproof/static/src/img/wbuilder/template-header-opt.svg'" attrs="{ style: 'width: calc(100% - 0.5rem);' }" />
>       </BuilderSelectItem>
>    </xpath>
>  </t>
> ```

| Attribute | Description |
| :--- | :--- |
| **views** | The template(s) to enable |
| **vars** | The name given to the variable (same as used into `primary_variables.scss`) |
| **checkVars** | Determine if `vars` are compared to set the option status. |
| **src** (in `Img`) | The thumbnail of the custom template shown in the templates selection on the Website Builder |

Now you have to explicitly define that you want to use your custom template in the Odoo SASS variables.

> `/website_airproof/static/src/scss/primary_variables.scss`
> ```scss
> $o-website-values-palettes: (
>    (
>       'header-template': 'airproof',
>    ),
> );
> ```

**Template**

> `/website_airproof/views/website_templates.xml`
> ```xml
> <template id="header" inherit_id="website.layout" name="Airproof - Header" active="True">
>    <xpath expr="//header//nav" position="replace">
>       <!-- Static Content -->
>       <!-- Components -->
>       <!-- Editable areas -->
>    </xpath>
> </template>
> ```

Don’t forget to adapt the `template_header_mobile` accordingly to keep consistency between desktop and mobile:

> `website_airproof/views/website_templates.xml`
> ```xml
> <template id="template_header_mobile" inherit_id="website.template_header_mobile" name="Airproof - Template Header Mobile">
>    <!-- Xpaths -->
> </template>
> ```

### Components

In your custom header, you can call several sub-templates using the `t-call` directive from QWeb:

#### Logo

```xml
<t t-call="website.placeholder_header_brand"
   _link_class.f="..." />
```

> **Important**: Don’t forget to create a record of the website logo in the database.

#### Menu

```xml
<t t-foreach="website.menu_id.child_id" t-as="submenu">
   <t t-call="website.submenu"
      item_class.f="nav-item"
      link_class.f="nav-link" />
</t>
```

#### Sign in

```xml
<t t-call="portal.placeholder_user_sign_in"
   _item_class.f="nav-item"
   _link_class.f="nav-link" />
```

#### User dropdown

```xml
<t t-call="portal.user_dropdown"
   _user_name="true"
   _icon="false"
   _avatar="false"
   _item_class.f="nav-item dropdown"
   _link_class.f="nav-link"
   _dropdown_menu_class.f="..." />
```

#### Language selector

```xml
<t t-call="website.placeholder_header_language_selector"
   _div_classes.f="..." />
```

#### Call to action

```xml
<t t-call="website.placeholder_header_call_to_action"
   _div_classes.f="..." />
```

#### Navbar toggler

```xml
<t t-call="website.navbar_toggler"
   _toggler_class.f="..." />
```

## Footer

By default, the footer contains a section with some static content. You can easily add new elements or create your own template.

### Standard

Enable one of the default footer templates. Don’t forget that you may need to disable the active footer template first.

> **Example**: `/website_aiproof/data/presets.xml`
> ```xml
> <record id="website.footer_custom" model="ir.ui.view">
>    <field name="active" eval="False" />
> </record>
> ```

> `/website_airproof/static/src/scss/primary_variables.scss`
> ```scss
> $o-website-values-palettes: (
>    (
>       'footer-template': 'Links',
>    ),
> );
> ```

> `/website_airproof/data/presets.xml`
> ```xml
> <record id="website.template_footer_links" model="ir.ui.view">
>    <field name="active" eval="True" />
> </record>
> ```

### Custom

Create your own template and add it to the list. Don’t forget that you may need to disable the active footer template first.

**Option**

> `/website_airproof/static/src/website_builder/footer_option_plugin.js`
> ```js
> import { Plugin } from "@html_editor/plugin";
> import { registry } from "@web/core/registry";
> import { _t } from "@web/core/l10n/translation";
> import { FooterTemplateChoice } from "@website/builder/plugins/options/footer_template_option";
>
> export class AirproofFooterOptionPlugin extends Plugin {
>    static id = "airproofFooterOption";
>    resources = {
>       footer_templates_providers: () => [
>          {
>             key: "airproof",
>             Component: FooterTemplateChoice,
>             props: {
>                title: _t("Airproof"),
>                view: "website_airproof.footer",
>                varName: "airproof",
>                imgSrc: "/website_airproof/static/src/img/wbuilder/template-footer-opt.svg",
>             },
>          },
>       ],
>    };
> }
>
> registry.category("website-plugins").add(AirproofFooterOptionPlugin.id, AirproofFooterOptionPlugin);
> ```

| Property | Description |
| :--- | :--- |
| **title** | Display title of the template |
| **view** | Template that is enabled. |
| **varName** | Value used in `primary_variables.scss` under `footer-template`. |
| **imgSrc** | The thumbnail of the custom template shown in the templates selection on the Website Builder |

**Declaration**

> `/website_airproof/static/src/scss/primary_variables.scss`
> ```scss
> $o-website-values-palettes: (
>    (
>       'footer-template': 'airproof',
>    ),
> );
> ```

**Template**

> `/website_airproof/views/website_templates.xml`
> ```xml
> <template id="footer" inherit_id="website.layout" name="Airproof - Footer" active="True">
>    <xpath expr="//div[@id='footer']" position="replace">
>       <div id="footer" class="oe_structure oe_structure_solo" t-ignore="true" t-if="not no_footer">
>          <!-- Content -->
>       </div>
>    </xpath>
> </template>
> ```

## Copyright

There is only one template available at the moment for the copyright bar.

To replace the content or modify its structure, you can add your own code to the following XPath.

> `/website_airproof/views/website_templates.xml`
> ```xml
> <template id="copyright" inherit_id="website.layout">
>    <xpath expr="//div[hasclass('o_footer_copyright')]" position="replace">
>       <div class="o_footer_copyright" data-name="Copyright">
>          <!-- Content -->
>       </div>
>    </xpath>
> </template>
> ```

## Drop zone

Instead of defining the complete layout of a page, you can create building blocks (snippets) and let the user choose where to drag and drop them, creating the page layout on their own. We call this *modular design*.

You can define an empty area that the user can fill with snippets.

```xml
<div id="oe_structure_layout_01" class="oe_structure" />
```

| Class | Description |
| :--- | :--- |
| **oe_structure** | Define a drag-and-drop area for the user. |
| **oe_structure_solo** | Only one snippet can be dropped in this area. |
| **oe_structure_not_nearest** | If a building block is dropped outside of a Drop zone having this class, the block will be moved in the nearest Drop Zone. |

You can also populate an existing drop zone with your content.

```xml
<template id="oe_structure_layout_01" inherit_id="..." name="...">
   <xpath expr="//*[@id='oe_structure_layout_01']" position="replace">
      <div id="oe_structure_layout_01" class="oe_structure oe_structure_solo">
         <!-- Content -->
      </div>
   </xpath>
</template>
```

## Responsive

Odoo in general relies on the Bootstrap framework which eases the responsiveness of your website on desktop and mobile. You can mainly take action on 3 aspects:

1. Automatic computed font sizes depending on the device
2. Column sizes on desktop (the columns are automatically stacked on mobile)
3. Visibility conditions (Show/Hide something on desktop/mobile)

### Font sizes

In Bootstrap 5, responsive font sizes are enabled by default, allowing text to scale more naturally across device and viewport sizes (relying on the `$enable-rfs` variable).

### Column sizes

Bootstrap uses a grid made of rows and columns to layout a page. Thanks to this structure, columns can be sized differently on mobile and desktop. In this version, the Website Builder allows to set mobile sizes (`col-12` for example) and desktop ones (`col-lg-4` for example) but not the medium breakpoints (`col-md-4` for example).

> **Warning**: The medium sizes can be set but the end-user is not able to edit them within the Website Builder.

### Visibility conditions

In the Odoo Website Builder, entire sections or specific columns can be hidden on mobile or desktop. This functionality leverages Bootstrap along with Odoo-specific classes:

- `o_snippet_mobile_invisible`
- `o_snippet_desktop_invisible`

Hide a section on desktop:

```xml
<section
   class="s_text_block o_cc o_cc1 o_colored_level pt16 pb16 d-lg-none o_snippet_desktop_invisible"
   data-snippet="s_text_block"
   data-name="Text">
   <!-- Content -->
</section>
```

Hide a column on mobile:

```xml
<section
   class="s_text_block o_cc o_cc1 o_colored_level pt16 pb16"
   data-snippet="s_text_block"
   data-name="Text">
   <div class="container s_allow_columns">
      <div class="row">
         <div class="col-12 col-lg-6 d-none d-lg-block o_snippet_mobile_invisible">
            Column 1
         </div>
         <div class="col-12 col-lg-6">
            Column 2
         </div>
      </div>
   </div>
</section>
```

| Class | Description |
| :--- | :--- |
| **o_snippet_mobile_invisible** | It tells the Website Builder that the element is hidden and is using visibility conditions option. |
| **o_snippet_desktop_invisible** | It tells the Website Builder that the element is hidden **on desktop and** is using visibility conditions option. |
| **d-none** | Hide the element in every situation. |
| **d-lg-block** | Show the element from the “large” breakpoint (on desktop). |

> **Important**: `o_snippet_mobile_invisible` / `o_snippet_desktop_invisible` classes have to be specified to keep the visibility conditions option functional. Even if an element is hidden on desktop, the Website Builder displays a list of these elements allowing the end-user to force show the element and edit it without switching between mobile and desktop mode.
