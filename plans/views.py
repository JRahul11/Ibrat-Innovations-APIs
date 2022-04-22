from ast import excepthandler
from rest_framework.response import Response
from rest_framework.views import APIView
from plans.models import PlanModel
from plans.serializers import AddPlanSerializer


class GetPlans(APIView):


    def createPlanJson(self, valuePlan):
        object = {
            'id': valuePlan.id,
            'name': valuePlan.name,
            'price': valuePlan.price,
            'validity_in_days': valuePlan.validity_in_days,
            'voice': valuePlan.voice,
            'data_per_day': valuePlan.data_per_day,
            'sms_per_day': valuePlan.sms_per_day,
            'add_ons': valuePlan.add_ons
        }
        return object


    def sortPlans(self, valuePlan, valuePlansList, popularPlansList, annualPlansList):
        if valuePlan.category == 'Value Plans':
            valuePlansList.append(self.createPlanJson(valuePlan))
        elif valuePlan.category == 'Popular Plans':
            popularPlansList.append(self.createPlanJson(valuePlan))
        elif valuePlan.category == 'Annual Plans':
            annualPlansList.append(self.createPlanJson(valuePlan))


    def get(self, request):
        valuePlansList = []
        popularPlansList = []
        annualPlansList = []
        valuePlans = PlanModel.objects.all()
        
        for valuePlan in valuePlans:
            self.sortPlans(valuePlan, valuePlansList, popularPlansList, annualPlansList)
        
        return Response(
            {
                'valuePlans': valuePlansList,
                'popularPlans': popularPlansList,
                'annualPlans': annualPlansList
            },
            status = 200
        )



class AddPlan(APIView):
    
    def post(self, request):
        addPlanSerializer = AddPlanSerializer(data = request.data)

        if addPlanSerializer.is_valid():
            name = addPlanSerializer.data['name']
            category = addPlanSerializer.data['category']
            price = addPlanSerializer.data['price']
            validity_in_days = addPlanSerializer.data['validity_in_days']
            voice = addPlanSerializer.data['voice']
            data_per_day = addPlanSerializer.data['data_per_day']
            sms_per_day = addPlanSerializer.data['sms_per_day']
            add_ons = addPlanSerializer.data['add_ons']

            try:
                plan = PlanModel.objects.get(name = name)
                return Response(
                    {
                        'status': 'Error',
                        'message': 'Plan exists'
                    },
                    status = 500
                )
            except:
                PlanModel.objects.create(name=name, category=category, price=price, validity_in_days=validity_in_days, voice=voice, data_per_day=data_per_day, sms_per_day=sms_per_day, add_ons=add_ons)
                return Response(
                    {
                        'status': 'Success',
                        'message': 'Plan Added'
                    }
                )

        else:
            return Response(
                {
                    'status': 'Error',
                    'message': addPlanSerializer.errors
                },
                status = 500
            )
