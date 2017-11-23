# -*- coding: utf-8 -*-
from odoo import http

# class TnvAccount(http.Controller):
#     @http.route('/tnv_account/tnv_account/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tnv_account/tnv_account/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tnv_account.listing', {
#             'root': '/tnv_account/tnv_account',
#             'objects': http.request.env['tnv_account.tnv_account'].search([]),
#         })

#     @http.route('/tnv_account/tnv_account/objects/<model("tnv_account.tnv_account"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tnv_account.object', {
#             'object': obj
#         })

class Home(Home):

    @http.route('/web/login', type='http', auth="none")
    def web_login(self, redirect=None, **kw):
        cr = request.cr
        uid = openerp.SUPERUSER_ID
        param_obj = request.registry.get('ir.config_parameter')
        request.params['disable_footer'] = ast.literal_eval(param_obj.get_param(cr, uid, 'login_form_disable_footer')) or False
        request.params['disable_database_manager'] = ast.literal_eval(param_obj.get_param(cr, uid, 'login_form_disable_database_manager')) or False

        change_background = ast.literal_eval(param_obj.get_param(cr, uid, 'login_form_change_background_by_hour')) or False
        if change_background:
            # config_login_timezone = param_obj.get_param(cr, uid, 'login_form_change_background_timezone')
            # tz = config_login_timezone and pytz.timezone(config_login_timezone) or pytz.utc
            # current_hour = datetime.datetime.now(tz=tz).hour or 10
            # if (current_hour >= 0 and current_hour < 3) or (current_hour >= 18 and current_hour < 24): # Night
            #     request.params['background_src'] = param_obj.get_param(cr, uid, 'login_form_background_night') or ''
            # elif current_hour >= 3 and current_hour < 7: # Dawn
            #     request.params['background_src'] = param_obj.get_param(cr, uid, 'login_form_background_dawn') or ''
            # elif current_hour >= 7 and current_hour < 16: # Day
            #     request.params['background_src'] = param_obj.get_param(cr, uid, 'login_form_background_day') or ''
            # else: # Dusk
            #     request.params['background_src'] = param_obj.get_param(cr, uid, 'login_form_background_dusk') or ''
            imges = ['1', '2', '3', '4']
            request.params['background_src'] = '/odoo_web_login/static/src/img/'+random.choice(imges)+'.png'
        else:
            request.params['background_src'] = param_obj.get_param(cr, uid, 'login_form_background_default') or ''
        return super(Home, self).web_login(redirect, **kw)
