export class Ship{
    id;
    name;
    capacity;
    sailors;
    level;
}

function create_ship_card(ship,user){
    let card_wrapper = document.createElement('div');
    card.className ='col-md-4 mb-4';
    let card = document.createElement('div');
    card.className = 'card';
    let card_body = document.createElement('div');
    card_body.className = 'card-body text-center';
    card.appendChild(card);
    card.appendChild(card_body);

    card_body.appendChild(ship_image(ship.level))
    card_body.appendChild(ship_title(ship.name));
    card_body.appendChild(ship_data_icons(ship));
    card_body.appendChild(delete_ship_button(ship));
    card_body.appendChild(save_button(ship));

    return card_wrapper;
}

function delete_ship_button(ship) {}
function save_button(ship) {}

function ship_data_icons(ship) {
    let container = document.createElement('div');
    container.className = 'container';
    let row = document.createElement('div');
    row.className = 'row';
    container.appendChild(row);

    let icons = [
        {
            url: "static/resources/sailor.svg",
            value: ship.sailors ,
            alt: "edit"
        },
        {
            url: "static/resources/capacity.svg",
            value: ship.capacity ,
            alt: "capacity"
        },
        {
            url: "static/resources/stars-level.svg",
            value: ship.level ,
            alt: "level"
        },
    ]

    icons.forEach(i =>{
        let icon_wrapper= document.createElement('div');
        let input_wrapper = document.createElement('div');
        let image_wrapper = document.createElement('div');
        icon_wrapper.className = 'grid col-4 mb-3';
        input_wrapper.className = 'g-col-6';
        image_wrapper.className = 'g-col-6 icon-wrapper';

        let input = document.createElement('input');
        let image = document.createElement('img');

        image.src = i.url;
        image.alt = i.alt;
        image.className = "ship-icon h-100";

        input.type = 'text';
        input.value = i.value;
        input.placeholder = i.alt;
        input.className = "card-text h4 white";
        input.style.maxWidth="40px";
        input.style.backgroundColor="transparent";
        input.style.textAlign="center";
        input.style.outline="none";


        input_wrapper.appendChild(input);
        image_wrapper.appendChild(image);
        icon_wrapper.appendChild(input_wrapper);
        icon_wrapper.appendChild(image_wrapper);
        row.appendChild(icon_wrapper);
    });

    return container;
}

function ship_title(name) {
    let title_wrapper =document.createElement('div');
    title_wrapper.className = 'row align-items-center';
    let title_wrapper_body = document.createElement('div');
    title_wrapper_body.className = 'col-12';
    title_wrapper.appendChild(title_wrapper_body);
    let card_title = document.createElement('h5');
    card_title.className = 'card-title';
    card_title.innerHTML = ship.name;
    title_wrapper_body.appendChild(card_title);
    return title_wrapper;
}

function ship_image(level) {
    return undefined;
}

function send_data(formData, ship){

}