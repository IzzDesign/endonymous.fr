---
layout: articles
order: 95
title: EndoDico
subtitle: Dictionnaire et définitions des mots-clefs de l'endométriose et l'adénomyose, du cycle menstruel, du corps féminin.
category: Le savoir c'est le pouvoir
alt_img: femme lecture dictionnaire vocabulaire endometriose
title_img: "EndoDico"
og_image: endodico.png
og_twitter_img : https://cycliques.fr/assets/images/twitter-lien.png
previous: /savoir/savoir.html
publish_date: 2021-04-01
---
<div class="dico-block">
  <div class="dico">
    {% for p in site.pages %}
      {% if p.subcategory == 'Endodico' %}
        <div class="icone-dico {% if p.url == page.url %} glass {% endif %}">
          <a href="{{ p.url }}">{{ p.title }}</a>
        </div>
      {% endif %}
    {% endfor %}
  </div>
  <div class="dico-definition">
    <img src="/assets/images/svg/icones/dico-icone.svg" title="Icone Endodico" width="220" height="220">
    <p class="dinomik">Du vocabulaire et des définitions sur l'endométriose.</p>
  </div>
</div>