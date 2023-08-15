from odoo import http
from odoo import models, fields, api, _
from odoo.http import request

class AppeulGetHotels(http.Controller):
    @http.route('/hotels/', auth="public", type="json", methods=['POST'])
    def all_cities(self):
        hotels = http.request.env['hotel.hotel'].search_read([('active', '=', True)], ['id', 'name', 'description', 'image_1920', 'featured_amenity_ids'])

        for rec in hotels:
            rec["f_amenity_ids"] = http.request.env['feat.amenities'].search_read([('id', 'in', rec['featured_amenity_ids'])], ['id', 'icon', 'name'])
        return hotels

    @http.route('/hotel/<hotel_id>', type='http', auth='public', website=True)
    def hotel_info(self, hotel_id):

        #hotel = http.request.env['hotel.hotel'].search_read([('id', '=', hotel_id)], ['id', 'name', 'description', 'featured_amenity_ids'])
        hotel = http.request.env['hotel.hotel'].search([('id', '=', hotel_id)])
        r_types = http.request.env['product.product'].search([('hotel_id', '=', int(hotel_id))])
        rooms_datas = hotel.get_room_type_data(r_types)

        print('hotels', hotel)

        hotel_amenities = []
        for h in hotel:
            hotel_amenities = hotel.mapped('amenities_ids')
            #htl_bws = http.request.env['hotel.hotel'].browse(h.id)
            print('hotel brws', hotel_amenities)


        # hotel_amenities = http.request.env['hotel.amenities'].search_read([('id', 'in', [hotel.amenities_ids])],
        #                                                ['id', 'icon', 'name'])


        # room_images = hotel.hotel_image_ids
        # if hotel.room_ids:
        #     room_images = request.env['room.image'].search([('product_variant_id', 'in', hotel.room_ids.ids)])[:5]
        #r_types = hotel.room_ids.mapped('room_type')
        # a_types = hotel.get_booking_types(avalible_rooms, room_capacity)
        # r_types = request.env['hotel.room.type'].browse(a_types)
        # pricelist = request.website.get_booking_current_pricelist()
        booked_room = {}
        selected_datas = None
        #url = '/hotel/%s/booking' % (slug(hotel))


        #print(hotel_amenities)
        values = {
            'hotel': hotel,
            'r_types': r_types,
            # 'room_images': room_images,
            'rooms_datas': rooms_datas,
            'hotel_amenities': hotel_amenities or [],
            # 'select_cat_id': selected_datas.get('room_type').id if not select_cat_id and selected_datas else int(
            #     select_cat_id) or False,
            # 'selected_datas': selected_datas if selected_datas else None,
            # 'book_info': json.dumps(booked_room) if booked_room else json.dumps(booked_room),
            # 'bkeep': bkeep,
            # 'pricelist': pricelist
        }

        return request.render('theme_web_ap_travelagent.appeul_hotels_info', values)
