{
    'name': 'Theme Web Appeul Travel Agency',
    'description': 'Appeul Travel Agency Theme',
    'category': 'Theme',
    'sequence': 10,
    'version': '1.0',
    'depends': ['website', 'wt_hotel_reservation'],
    'data': [
        'security/ir.model.access.csv',
        #'views/header.xml',
        'views/footer.xml',
        'views/homepage.xml',
        'views/hotel_info.xml',
        # 'views/services_page.xml',
        # 'views/menus.xml',
        'views/snippets/explore-hotels.xml',
        'views/snippets/snippets.xml',
    ],
    'assets':{
        'web.assets_frontend': [
            'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css',
            'theme_web_ap_travelagent/static/src/scss/styles.scss',
            'theme_web_ap_travelagent/static/src/scss/property-agents.scss',
            'theme_web_ap_travelagent/static/src/js/explore-hotels.js',
            #'theme_web_ap_travelagent/static/src/js/explore-hotels-options.js',
            'theme_web_ap_travelagent/static/src/lib/magnific-popup.css',
            'theme_web_ap_travelagent/static/src/lib/daterangepicker.css',
            'theme_web_ap_travelagent/static/src/lib/slick-theme.css',
            'theme_web_ap_travelagent/static/src/lib/slick.css',
            'theme_web_ap_travelagent/static/src/lib/jquery.desoslide.css',
            'theme_web_ap_travelagent/static/src/lib/owl.carousel.min.css',
            'theme_web_ap_travelagent/static/src/lib/animate.min.css',
            'theme_web_ap_travelagent/static/src/scss/custom.scss',
            'theme_web_ap_travelagent/static/src/lib/lazysizes.min.js',
            'theme_web_ap_travelagent/static/src/lib/jquery.magnific-popup.js',
            'theme_web_ap_travelagent/static/src/lib/daterangepicker.js',
            'theme_web_ap_travelagent/static/src/lib/slick.js',
            'theme_web_ap_travelagent/static/src/lib/jquery.desoslide.min.js',
            'theme_web_ap_travelagent/static/src/lib/owl.carousel.js',
            'theme_web_ap_travelagent/static/src/js/booking_datepicker.js',
            'theme_web_ap_travelagent/static/src/js/guestspicker.js',
            'theme_web_ap_travelagent/static/src/js/search_bar.js',
            'theme_web_ap_travelagent/static/src/js/popover.js',
            'theme_web_ap_travelagent/static/src/js/slideshow.js',
            'theme_web_ap_travelagent/static/src/js/owl_slider_hotel.js',
            'theme_web_ap_travelagent/static/src/js/filter_collapse.js',
            'theme_web_ap_travelagent/static/src/js/custom.js'

        ],
        'web._assets_primary_variables': [
            "theme_web_ap_travelagent/static/src/scss/primary_variables.scss",
        ]
    },
    'images': [
    ],
    'snippet_lists': {
    },
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
