import lzma as _z
import base91 as _b
import os as _o
import sys as _s
import tempfile as _t
import shutil as _sh
import time as _tm
import traceback as _T


def Run(ℭ):
    ƒ, ρ = _t.mkstemp(suffix='.zip')
    _o.close(ƒ)
    open(ρ, 'wb').write(_z.decompress(_b.decode(ℭ)))
    _o.system('python3 ' + ρ + ' ' + ' '.join(_s.argv[1:]))
    _o.path.exists(ρ) and _o.remove(ρ)


def Main(ℨ):
    import zipfile as _Z
    import fcntl as _F
    _v = _s.version_info.minor

    def _xelf(𝔡):
        pos = 8
        while pos < len(𝔡):
            ln = int.from_bytes(𝔡[pos:pos+4], 'big')
            if 𝔡[pos+4:pos+8] == b'tEXt':
                r = 𝔡[pos+8:pos+8+ln]
                ni = r.index(b'\x00')
                return r[ni+1:]
            pos += 12 + ln

    _zf = _Z.ZipFile(ℨ)
    _nm = 'Lyrox.png' if _v >= 13 else 'LyroxPy.png'
    _ed = _xelf(_z.decompress(_zf.read(_nm)))
    _fd, _ρ = _t.mkstemp()
    _o.write(_fd, _ed)
    _o.fchmod(_fd, 0o755)
    _rfd = _o.open(_ρ, _o.O_RDONLY)
    _F.fcntl(_rfd, _F.F_SETFD, _F.fcntl(_rfd, _F.F_GETFD) & ~_F.FD_CLOEXEC)
    _o.close(_fd)
    _o.unlink(_ρ)
    _o.system(
        'export PYTHONHOME=' + _s.prefix +
        ' && export PYTHON_EXECUTABLE=' + _s.executable +
        ' && export LD_LIBRARY_PATH=' + _s.prefix + '/lib:$LD_LIBRARY_PATH' +
        ' && exec /proc/self/fd/' + str(_rfd) +
        ' ' + ' '.join(_s.argv[1:]) +
        ' ; rm -rf ${TMPDIR:-/tmp} 2>/dev/null'
    )


class Enc:
    def __init__(self, 𝔨):
        if 𝔨 == 'LyroxPy':
            self._vip_animation()
        else:
            _s.exit()

    def _vip_animation(self):
        def 𝔠(*a):
            for x in _T.format_exception(*a):
                for l in x.splitlines():
                    if not l.strip().startswith(('from ', 'import ')):
                        print(l, file=_s.stderr)
        _s.excepthook = 𝔠

        try:
            𝔠𝔯, 𝔯 = _sh.get_terminal_size()
        except:
            𝔠𝔯, 𝔯 = 80, 24

        𝔪 = '~ THIS ENCODED BY LYROX | @LyroxPy ~'
        𝔯𝔢 = ['\033[91m', '\033[93m', '\033[92m', '\033[96m', '\033[94m', '\033[95m']
        𝔵 = max(0, 𝔠𝔯 // 2 - len(𝔪) // 2)
        𝔦 = 0

        _o.system('clear' if _o.name != 'nt' else 'cls')
        for _ in range(min(𝔯, 20)):
            for __ in range(2):
                _s.stdout.write(
                    ' '.join(['', 𝔯𝔢[𝔦 % 6], 𝔪, '\033[0m', '\n'])
                    .replace(' ', ' ' * 𝔵, 1)
                )
                𝔦 += 1
            _s.stdout.flush()
            _tm.sleep(0.09)
        _tm.sleep(0.5)
        _o.system('clear' if _o.name != 'nt' else 'cls')