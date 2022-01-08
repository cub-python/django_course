
{% extends "mainapp/base.html" %}
{% load static %}

{% block content %}
    {% include 'ordersapp/includes/inc_order_summary.html' %}
    <div class="basket_list">
        {% for item in object.orderitems.select_related %}
            <div class="basket_record">
                <img style="height: 150px" src="{{ item.product.image.url }}"
                     alt="{{ item.product.short_desc }}">
                <span class="category_name">
                   {{ item.product.category.name }}
               </span>
                <span class="product_name">{{ item.product.name }}</span>
                <span class="product_price">
                   {{ item.product.price }}&nbspруб
               </span>
                <span class="product_quantitiy">
                   x {{ item.quantity }} шт.
               </span>
                <span class="product_cost">
                    = {{ item.get_product_cost }}&nbspруб
               </span>
            </div>
        {% endfor %}
    </div>
    {% include 'ordersapp/includes/inc_order_actions.html' %}

{% endblock %}