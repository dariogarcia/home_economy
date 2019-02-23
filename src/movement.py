# coding: utf-8

categories = {}
categories.update({'hipoteca':['Transferencia',
                            'dico recibido',
                            'dico emitido',
                            'hipoteca',
                            'Hipoteca',
                            'MATERNIDAD',
                            'prestamo',
                            'Traspaso emitido',
                            'Traspaso recibido',
                            ]})
categories.update({'roba':['PRIVEE',
                    'Showroom',
                    'PRIVALIA',
                    'Privalia',
                    'TUC TUC',
                    'KIABI',
                    'TETATET',
                    'PICCOLLETTI',
                    'MERCERIA',
                    'HAPPY FRIDAY',
                    'VERTBAUDET',
                    'AMICS ESPLUGUES',
                    ]})
categories.update({'amazon':['AMZN',
                            'AMAZON',
                            'Amazon',
                            'amazon']})
categories.update({'menjar_domicili':['BIOCHEF',
                                        'VIENA',
                                        'PIZZA MARKET',
                                        'ANEL',
                                        'ENOTECA PIRAS',
                                        'SIN VERGUENZA',
                                        'RESTAURANTE',
                                        ]})
categories.update({'menjar':['DIA',
                            'A LA CART',
                            'DGUSTA',
                            'SERVIFRUIT',
                            'CONDIS',
                            'CAPRABO',
                            'ALCAMPO',
                            'CARNISSERIA',
                            'CORTE INGLES',
                            'EL CELLER',
                            'ALDI',
                            'LA SIRENA',
                            'MERCADONA',
                            'FRUITES I VERDURES',
                            'CA LA REMEI ESPL',
                            'ALBERTMAT',
                            'ENRIC ECO',
                            ]})
categories.update({'rebuts':['YELLOW ENERGY',
                            'VOLKSWAGEN',
                            'CULEBRAS',
                            'Seguro',
                            'AIGUES DE BARCELONA',
                            'COM PROP CL LA VINYA',
                            'BENS IMMOBLES',
                            'AQUALOGY',
                            'NIMBONENS',
                            'RECIBO H.C.  Energia',
                            'EUROPOLIS',
                            'LLAR INFANS NIMBO'
                            ]})
categories.update({'panaderies':['TINYOL',
                                'BOULANGERIE',
                                'CLARITA',
                                'CIABBATTA',
                                'FIGULS',
                                'LA REPOSADA',
                                ]})
categories.update({'menjarextra':['GRANER DE LA SUSI',
                            'VERITAS',
                            'CENTRE DIETETIC CASELLAS',
                            'CELLER TORRAS',
                            ]})
categories.update({'extras':['DEL RETAL',
                            'CUCA DE LLUM',
                            'Photobox',
                            'TEATRES',
                            'ABACUS',
                            'TOUS',
                            'DECIMAS',
                            'DUET',
                            'DRIM',
                            'REDBUBBLE',
                            'DECATHLON',
                            'PARTY FIESTA',
                            'ARTESANS DE LABEL',
                            'HAIKU BARCELONA',
                            'BAZAR ORIENTAL ESPL',
                            'RUIXIANG 2013',
                            'JUGUETERIA MAINADA',
                            'XIAO FENG 2017',
                            'Pago S.E.DE CORREOS',
                            'TICKETEA MADRID',
                            'JOYERIA',
                            'SALTIMBANQUI',
                            'RESIN',
                            'SOULD PARK',
                            'TICKETMASTER',
                            'BUMBUETA',
                            ]})
categories.update({'cotxe':['ES LA SARDANA',
                            'ZONA BLAVA ESTACIONAMENT',
                            'PARKING',
                            'Pago AP.',
                            'SERVEI CATALA DE TRANSIT',
                            'GRUES BCN',
                            'A.C.E.S.A',
                            'CEDIPSA',
                            'INVICAT',
                            'GASAOLINERA',
                            'PARK.MARQUES',
                            ]})
categories.update({'fungibles':['FARMACIA',
                            'AUBERT',
                            'FACIL MOBEL',
                            'ENTRECORTINES',
                            'ELECTRILAMP',
                            'FERRETERIA MUSTE',
                            'IKEA',
                            ]})
categories.update({'cash':['Cargo cajero',
                            'Reintegro Cajero',
                            ]})

class Movement:
    

    def __init__(self, date, description, amount):
        self.date = date
        self.description = description
        self.amount = amount
        self.category = None



    def assign_category(self):
        found_categories = set()
        for cat_name,cat_terms in categories.items():
            for term in cat_terms:
                if term in self.description:
                    found_categories.add(cat_name)
        if len(found_categories) == 0:
            print('Category not found for:',self.description,self.amount)
        if len(found_categories) == 2 and 'hipoteca' in found_categories:
            found_categories.remove('hipoteca')
        if len(found_categories) >= 2:
            print('Multiple categories found for:',self.description,':',found_categories)
