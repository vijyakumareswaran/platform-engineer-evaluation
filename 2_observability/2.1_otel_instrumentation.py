from opentelemetry import trace, baggage
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource
from opentelemetry.context import attach

# Setup
trace.set_tracer_provider(
    TracerProvider(resource=Resource.create({"service.name": "payment-service"}))
)
otlp_exporter = OTLPSpanExporter(endpoint="http://localhost:4317", insecure=True)
trace.get_tracer_provider().add_span_processor(BatchSpanProcessor(otlp_exporter))
tracer = trace.get_tracer(__name__)

def process_payment(user_id: str, payment_method: str):
    # Add baggage
    ctx = baggage.set_baggage("user.id", user_id)
    attach(ctx)

    with tracer.start_as_current_span("process_payment", context=ctx) as span:
        span.set_attribute("payment.method", payment_method)
        # Payment processing logic
        print(f"Processing payment for {user_id} via {payment_method}")
        return f"Payment processed for {user_id}"