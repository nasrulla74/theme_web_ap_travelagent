/** @odoo-module **/

import publicWidget from 'web.public.widget';

publicWidget.registry.TestApHotels = publicWidget.Widget.extend({
    selector: '.explore-hotels',

    /**
     * @override
     */
    start() {
//        console.log('TestApHotels')
//        console.log(this.el)
//        console.log(this.el.querySelector('#ap-hotels-row'))

        let hotelsRow = this.el.querySelector('#ap-hotels-row')

        if (hotelsRow){


            this._rpc({
                route: '/hotels/',
                params:{}
                    }).then(data=>{
                        console.log(data)
                        let html = ``
                                data.forEach(r=>{
                                    html += `<div class="card" style="width: 18rem; padding-right: 0; padding-left: 0; margin: 1rem">
                                  <img class="card-img-top" src="data:image/png;base64,${r.image_1920}" alt="Card image cap"/>
                                  <div class="card-body">
                                    <h5 class="card-title">${r.name}</h5>
                                    <p class="card-text text-black-50"><small>${r.description}</small></p>
                                  </div>

                                    <div class="text-center ml-2">`

                                        console.log(r.f_amenity_ids)
                                        r.f_amenity_ids.forEach(fa=>{
                                            console.log(fa.icon)
                                             html += `

                                                <span class="px-2 ">
                                                          <img src="data:image/svg+xml;base64,${fa.icon}" />

                                                            </span>`
//                                             html += `<span class="px-2">
//                                                          <img src="data:image/png;base64,${fa.icon}" width="30" height="30"/>
//
//                                                            </span>`

                                        })


                                    html += `
                                    </div>

                                  <div class="card-footer bg-transparent border-light text-center mt-3">

                                      <a href="/hotel/${r.id}" class="btn btn-primary onb_btn mt32">REQUEST QUOTATION</a>

                                    </div>


                                </div>`
                                })
                                hotelsRow.innerHTML = html

                    })
        }


    },
});

export default publicWidget.registry.TestApHotels;
