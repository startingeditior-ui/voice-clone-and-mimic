"""
tests/test_rvc_env.py — Smoke test for the RVC voice conversion pipeline.

Run from the project root with the rvc_env active:
    rvc_env\Scripts\activate
    python -m tests.test_rvc_env

Requires:
  - Retrieval-based-Voice-Conversion-WebUI/ to be cloned alongside this project
  - At least one .pth model in Retrieval-based-Voice-Conversion-WebUI/assets/weights/
  - input/recorded.wav for a live conversion test (optional)
"""

import os
import sys

# Ensure the project root is on the path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

RVC_ROOT = os.path.join(PROJECT_ROOT, "Retrieval-based-Voice-Conversion-WebUI")

try:
    from src.rvc_wrapper import RVCWrapper
    print(f"✅ Successfully imported RVCWrapper")

    # Initialize
    rvc = RVCWrapper()
    print("✅ Successfully initialized RVCWrapper")

    # Check for models
    weights_dir = os.path.join(RVC_ROOT, "assets", "weights")
    if not os.path.isdir(weights_dir):
        print(f"❌ Weights directory not found: {weights_dir}")
        sys.exit(1)

    models = [f for f in os.listdir(weights_dir) if f.endswith(".pth")]

    if not models:
        print("⚠️  No .pth models found in RVC weights directory.")
        print(f"   Expected: {weights_dir}")
        print("   Skipping model-load and conversion tests.")
    else:
        model_name = models[0]
        print(f"Loading model: {model_name}")
        rvc.load_model(model_name)
        print(f"✅ Model '{model_name}' loaded successfully")

        # Test conversion if recorded.wav exists
        source = os.path.join(PROJECT_ROOT, "input", "recorded.wav")
        output = os.path.join(PROJECT_ROOT, "output", "test_mimic_rvc_env.wav")
        os.makedirs(os.path.dirname(output), exist_ok=True)

        if os.path.exists(source):
            print(f"Converting {source}...")
            rvc.convert(source, output, f0_method="rmvpe")
            print(f"✅ Conversion successful! Output: {output}")
        else:
            print(f"⚠️  input/recorded.wav not found — skipping live conversion test.")
            print("   Place a WAV file at input/recorded.wav to enable this test.")

except Exception as e:
    import traceback
    traceback.print_exc()
    print(f"❌ Error: {e}")
