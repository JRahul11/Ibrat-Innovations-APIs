from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import UserModel
from plans.models import PlanModel
from subscriptions.models import SubscriptionModel
from subscriptions.serializers import ValidationSerializer

# Accepts POST Request
class RechargePlan(APIView):


    def post(self, request):
        # Validate data using Serializer
        validateSerializer = ValidationSerializer(data = request.data)

        if validateSerializer.is_valid():
            phone_number = validateSerializer.data['phone_number']
            plan_id = validateSerializer.data['plan_id']

            try:
                # Get user reference
                user = UserModel.objects.get(phone_number=phone_number)                         
                # Get plan reference
                plan = PlanModel.objects.get(id=plan_id)

                try:
                    # Check if user has an active plan
                    subscription = SubscriptionModel.objects.get(user=user, is_active=True)
                    # Create a new upcoming plan
                    SubscriptionModel.objects.create(user=user, plan=plan, is_active=False)
                    return Response(
                        {
                            'status': 'Success',
                            'message': 'Plan is setted as upcoming plan'
                        },
                        status = 200
                    )
                except:
                    # Create a new active plan
                    SubscriptionModel.objects.create(user=user, plan=plan, is_active=True)
                    return Response(
                        {
                            'status': 'Success',
                            'message': 'Plan is setted as active plan'
                        },
                        status = 200
                    )

            # If user or plan does not exist
            except:
                return Response(
                    {
                        'status': 'Error',
                        'message': 'User or Plan does not exist',
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

