# Pages

In this chapter, you will learn how to declare static pages.

## Default pages

In Odoo, websites come with a few default static pages (Home, Contact us, 404, …). They are built the following way.

`/website/data/website_data.xml`
```xml
<template id="website.homepage" name="Home">
   <t t-call="website.layout"
      pageName.f="homepage">
      <div id="wrap" class="oe_structure oe_empty" />
   </t>
</template>
```

Each default page is a template with its own content saved into a record. This is the reason why custom pages are created within a record.

The `<t-call='website.layout'>` has some variables that can be set:

**Define the meta title**

```xml
<t t-call="website.layout"
   additional_title.translate="My Page Title">
   <div id="wrap" class="oe_structure oe_empty" />
</t>
```

> **Tip**: As the `t-call` accepts parameters, these can be passed as variable, string (`*.f`) or translatable string (`*.translate`).

**Define the meta description**

```xml
<t t-call="website.layout"
   meta_description.translate="This is the description of the page that will appear on Search Engines.">
   <div id="wrap" class="oe_structure oe_empty" />
</t>
```

**Add a CSS class to the page**

```xml
<t t-call="website.layout"
   pageName.f="homepage">
   <div id="wrap" class="oe_structure oe_empty" />
</t>
```

**Deactivate default pages**

If needed, deactivate default pages.

`/website_airproof/data/pages/home.xml`
```xml
<record id="website.homepage" model="ir.ui.view">
    <field name="active" eval="False" />
</record>
```

`/website_airproof/data/pages/contactus.xml`
```xml
<record id="website.contactus" model="ir.ui.view">
    <field name="active" eval="False" />
</record>
```

**Replace default content**

Alternatively, replace the default content of these pages using XPath.

`/website_airproof/data/pages/404.xml`
```xml
<template id="404" inherit_id="http_routing.404">
   <!-- Change the meta title parameter through the t-call -->
   <xpath position="attributes" expr="//t[@t-call='web.frontend_layout">
      <attribute name="additional_title.translate">404 - Not found</attribute>
   </xpath>
   <!-- Replace the default content -->
   <xpath expr="//*[@id='wrap']" position="replace">
      <div id="wrap" class="oe_structure">
         <!-- Content -->
      </div>
   </xpath>
</template>
```

## Theme pages

You can add as many pages as you want to your website. Instead of defining a `<template>`, create a page record.

**Declaration**

`/website_airproof/data/pages/about_us.xml`
```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo noupdate="1">
   <record id="page_about_us" model="website.page">
      <field name="name">About us</field>
      <field name="is_published" eval="True" />
      <field name="key">website_airproof.page_about_us</field>
      <field name="url">/about-us</field>
      <field name="website_id" eval="1" />
      <field name="type">qweb</field>
      <field name="arch" type="xml">
         <t t-name="website_airproof.page_about_us">
            <t t-call="website.layout">
               <div id="wrap" class="oe_structure">
                  <!-- Content -->
               </div>
            </t>
         </t>
      </field>
   </record>
</odoo>
```

> **Tip**: To set the page as the homepage, set the field below:
> ```xml
> <field name="is_homepage" eval="True" />
> ```

> **Tip**: Header and footer are visible by default but can be hidden on specific pages by setting `header_visible` and/or `footer_visible` fields to `false`. This way they are visually hidden but still there in the DOM. Both can be displayed again through the Website Builder like any hidden elements hidden under a **Visibility Condition**.
> ```xml
> <field name="header_visible" eval="False" />
> <field name="footer_visible" eval="False" />
> ```
> The Header can be hidden on all pages by enabling this view:
>
> `/website_airproof/data/presets.xml`
> ```xml
> <record id="website.option_layout_hide_header" model="ir.ui.view">
>    <field name="active" eval="True" />
> </record>
> ```

> **Multiwebsite and website_id**: In a module context, the record created above is available, by default, on every website available on the database. It’s preferable to specify the `website_id` of the website where the page will be findable.

| Field | Description |
| :--- | :--- |
| **name** | Page name (human-readable). |
| **is_published** | Define if the page is published (visible to visitors). |
| **key** | View key (must be unique) |
| **url** | Relative path where the page is reachable. |
| **type** | View type |
| **arch** | View architecture (the markup of your page) |

With `<t t-call="website.layout">` you use the Odoo default page layout with your code.

### `noupdate` attribute

This attribute prevents data overwriting. It can be added either on a `data` tag wrapping some records to protect or on the `odoo` tag in order to protect all records declared into the file.

**Protect all records of the file:**

```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo noupdate="1">
   <record id="menu_company" model="website.menu">
      <!-- Fields -->
   </record>
   <record id="menu_faq" model="website.menu">
      <!-- Fields -->
   </record>
</odoo>
```

**Protect specific records in the file:**

```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
   <record id="menu_company" model="website.menu">
      <!-- Fields -->
   </record>

   <data noupdate="1">
      <record id="menu_faq" model="website.menu">
         <!-- Fields -->
      </record>
      <record id="menu_legal" model="website.menu">
         <!-- Fields -->
      </record>
   </data>
</odoo>
```

**Use case**

There are several static pages created in the module. This one has been installed on the database and the end-user has updated some of those pages. Some bug fixes must be applied on the static pages while avoiding any loss of changes made by the end-user.

**Problem**

In case of a module update on the database, every record declared into the module will overwrite those existing in the database even if the end-user has changed some of these records.

**Solution**

By wrapping the record (or all records declared in the file) into a `<data noupdate="1"></data>` tag, the record declared is created at the first module installation but not updated after a module update.

> **Note**: If a record has been manually deleted (e.g.: a menu item), the system detects that this record doesn’t exist and will re-create it. This method is usable for every type of records.

### Header overlay

Make the header background transparent and stand on top of the page content.

```xml
<field name="header_overlay" eval="True"/>
```

> **Note**: To create the content of a static page, use the Odoo way of doing things in order to remain editable by the Website Builder. Odoo takes advantage of Bootstrap framework (5.3).

### Page templates

Create preset static page templates available from the New Page dialog window.

**Declaration**

The page templates has to be defined into the `__manifest__.py` of the module through `new_page_templates` and `new_page_template_templates.xml`:

`/website_airproof/__manifest__.py`
```python
{
   'name': 'Airproof Theme',
   # ...
   'depends': ['website'],
   'data': [
      # ...
      'views/new_page_template_templates.xml'
   ],
   # ...
   'new_page_templates': {
      'airproof': {
         'faq': ['s_airproof_text_block_h1', 's_title', 's_faq_collapse', 's_call_to_action']
   }
}
```

**Templates**

Then you have to create the template using a specific naming convention based on the hierarchy into the `__manifest__.py`. In this case, the name is `new_page_template_sections_airproof_faq`.

Create a new instance of the standard `s_text_block` (`primary` attribute is important) and apply some adaptations:

`/website_airproof/views/new_page_template_templates.xml`
```xml
<template id="s_airproof_text_block_h1" inherit_id="website.s_text_block" primary="True">
   <xpath expr="//div[hasclass('container')]|//div[hasclass('o_container_small')]" position="replace">
      <div class="container s_allow_columns">
            <h1 class="display-1">FAQ - Help</h1>
      </div>
   </xpath>
</template>
```

Instantiate each building block (modified or not) for the page template:

`/website_airproof/views/new_page_template_templates.xml`
```xml
<template id="new_page_template_airproof_faq_s_text_block_h1" inherit_id="website_airproof.s_airproof_text_block_h1" primary="True" />
<template id="new_page_template_airproof_faq_s_title" inherit_id="website.s_title" primary="True" />
<template id="new_page_template_airproof_faq_s_faq_collapse" inherit_id="website.s_faq_collapse" primary="True" />
<template id="new_page_template_airproof_faq_s_call_to_action" inherit_id="website.s_call_to_action" primary="True" />
```

Then, create your page template with some `t-snippet-call` within an `#wrap`:

`/website_airproof/views/new_page_template_templates.xml`
```xml
<template id="new_page_template_sections_airproof_faq" name="Airproof - New Page Template FAQ">
   <div id="wrap">
      <t t-snippet-call="website_airproof.new_page_template_airproof_faq_s_text_block_h1" />
      <t t-snippet-call="website_airproof.new_page_template_airproof_faq_s_title" />
      <t t-snippet-call="website_airproof.new_page_template_airproof_faq_s_faq_collapse" />
      <t t-snippet-call="website_airproof.new_page_template_airproof_faq_s_call_to_action" />
   </div>
</template>
```

**Custom Groups**

Once the page template is created, create a custom group and add it to the existing ones.

`/website_airproof/views/new_page_template_templates.xml`
```xml
<template id="new_page_template_groups" inherit_id="website.new_page_template_groups" name="Airproof - New Page Template Groups">
   <xpath expr="//div[@id='custom']" position="after">
      <div id="airproof">Airproof</div>
   </xpath>
</template>
```
