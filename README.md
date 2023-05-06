# Automatic Drum Transcription Library (ADTLib)

The automatic drum transcription (ADT) library contains open source ADT algorithms to aid other researchers in areas of music information retrieval (MIR). The algorithms return both a .txt file of kick drum, snare drum, and hi-hat onsets and an automatically generated drum tabulature. 

## This Fork
- Focused on the Python function only
- Update code to work with Tensorflow 2.x
- Switch off default text and tab export
- Instead of an array of file paths, pass _one_ file path or signal data
- Expose sample rate and number of channels (original library assumed 44100Hz and Mono)

## Installation

`pip install git+https://github.com/brunoimbrizi/ADTLib.git`

## Usage

#### Python function

```Python
ADT(data, sample_rate=None, num_channels=1, text='no', tab='no', save_dir=None, output_act='no')
```
| Name           | Description                                         | Default |
| -------------- | --------------------------------------------------- | ------- |   
| `data`         | Signal data or file name or file handle.            |         |
| `sample_rate`  | Desired sample rate of the signal [Hz], or 'None' to return the signal in its original rate. | `22050` |
| `num_channels` | Reduce or expand the signal to `num_channels` channels, or 'None' to return the signal with its original channels. | `1` |

Other parameters: refer to the [original repository](https://github.com/CarlSouthall/ADTLib).

#### Example

```Python
from ADTLib import ADT

out = ADT('drums.wav')
```

```Python
from ADTLib import ADT
import librosa

y, sr = librosa.load(path='drums.mp3')
out = ADT(y, sample_rate=sr)
```

## License / References / Help

Refer to the [original repository](https://github.com/CarlSouthall/ADTLib).

