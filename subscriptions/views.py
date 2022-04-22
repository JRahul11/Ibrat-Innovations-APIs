from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import UserModel
from plans.models import PlanModel
from subscriptions.models import SubscriptionModel
from subscriptions.serializers import ValidationSerializer


class RechargePlan(APIView):


    def post(self, request):
        validateSerializer = ValidationSerializer(data = request.data)

        if validateSerializer.is_valid():
            phone_number = validateSerializer.data['phone_number']
            plan_id = validateSerializer.data['plan_id']

            try:
                user = UserModel.objects.get(phone_number=phone_number)
                plan = PlanModel.objects.get(id=plan_id)

                try:
                    subscription = SubscriptionModel.objects.get(user=user, is_active=True)
                    SubscriptionModel.objects.create(user=user, plan=plan, is_active=False)
                    return Response(
                        {
                            'status': 'Success',
                            'message': 'Plan is setted as upcoming plan'
                        },
                        status = 200
                    )
                except:
                    SubscriptionModel.objects.create(user=user, plan=plan, is_active=True)
                    return Response(
                        {
                            'status': 'Success',
                            'message': 'Plan is setted as active plan'
                        },
                        status = 200
                    )

            except Exception as e:
                return Response(
                    {
                        'status': 'Error',
                        'message': 'User or Plan does not exist',
                        'error_msg': str(e)
                    },
                    status = 500
                )

        else:
            return Response(
                {
                    'status': 'Error',
                    'message': validateSerializer.errors
                },
                status = 500
            )

