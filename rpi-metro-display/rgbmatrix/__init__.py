"""
Compatibility shim for rgbmatrix.

On Raspberry Pi, the real rpi-rgb-led-matrix bindings should be installed
system-wide and will be imported directly.
On other platforms, this uses RGBMatrixEmulator for development/testing.
"""
import sys
import platform

# Check if we're on a Raspberry Pi by looking for the real rgbmatrix
# in system site-packages (not this local shim)
_real_rgbmatrix = None

if platform.machine().startswith('aarch64') or platform.machine().startswith('arm'):
    # Might be a Pi - try to import the real library
    try:
        import importlib.util
        # Look for rgbmatrix in system paths, excluding the current package
        for path in sys.path:
            if 'site-packages' in path and 'rpi-metro-display' not in path:
                spec = importlib.util.find_spec('rgbmatrix', [path])
                if spec and spec.origin and 'rpi-rgb-led-matrix' in spec.origin:
                    _real_rgbmatrix = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(_real_rgbmatrix)
                    break
    except Exception:
        pass

if _real_rgbmatrix:
    RGBMatrix = _real_rgbmatrix.RGBMatrix
    RGBMatrixOptions = _real_rgbmatrix.RGBMatrixOptions
    graphics = _real_rgbmatrix.graphics
else:
    # Use the emulator
    from RGBMatrixEmulator import RGBMatrix, RGBMatrixOptions, graphics

__all__ = ['RGBMatrix', 'RGBMatrixOptions', 'graphics']
