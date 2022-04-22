from rest_framework.response import Response
from rest_framework.views import APIView
from users.serializers import AddUserSerializer
from users.models import UserModel
from subscriptions.models import SubscriptionModel



class Welcome(APIView):


    def get(self, request):
        return Response('Welcome to Ibrat Innovation APIs by Rahul Jadhav')



class AddUser(APIView):
    
    
    def post(self, request):
        addUserSerializer = AddUserSerializer(data = request.data)
        
        if addUserSerializer.is_valid():
            name = addUserSerializer.data['name']
            phone_number = addUserSerializer.data['phone_number']
            
            try:
                user = UserModel.objects.get(phone_number = phone_number)
                return Response(
                    {
                        'status': 'Error',
                        'message': 'Phone number already exists'
                    },
                    status = 500
                )
            except:
                UserModel.objects.create(name=name, phone_number=phone_number)
                return Response(
                    {
                        'status': 'Success',
                        'message': 'User Added'
                    },
                    status = 200
                )

        else:
            return Response(
                {
                    'status': 'Error',
                    'message': addUserSerializer.errors
                },
                status = 500
            )



class ViewUserPlan(APIView):


    def createPlanJson(self, userPlan):
        object  = {
            'id': userPlan.plan.id,
            'name': userPlan.plan.name,
            'category': userPlan.plan.category,
            'price': userPlan.plan.price,
            'validity_in_days': userPlan.plan.validity_in_days,
            'voice': userPlan.plan.voice,
            'data_per_day': userPlan.plan.data_per_day,
            'sms_per_day': userPlan.plan.sms_per_day,
            'add_ons': userPlan.plan.add_ons
        }
        return object


    def sortPlans(self, userPlan, activePlanList, upcomingPlanList):
        if not userPlan.is_active:
            upcomingPlanList.append(self.createPlanJson(userPlan))
        else:
            activePlanList.append(self.createPlanJson(userPlan))


    def post(self, request):
        activePlanList = []
        upcomingPlanList = []
        phone_number = request.data['phone_number']
        
        try:
            user = UserModel.objects.get(phone_number=phone_number)
            try:
                userPlans = SubscriptionModel.objects.filter(user=user)
                for userPlan in userPlans:
                    self.sortPlans(userPlan, activePlanList, upcomingPlanList)
                
                return Response(
                    {
                        'activePlan': activePlanList,
                        'upcomingPlan': upcomingPlanList
                    },
                    status = 200
                )
            except:
                return Response(
                    {
                        'status': 'Success',
                        'message': 'User do not have an active plan'
                    },
                    status = 200
                )

        except:
            return Response(
                {
                    'status': 'Error',
                    'message': 'User does not exists'
                },
                status = 500
            )