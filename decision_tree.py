# Decision Tree

import csv, random
from typing import Optional

class Song:
    """An object that represents a specific song and stores its various song attributes.

        Instance Attributes
        - name:
            Name of the song.
        - genre:
            Genre of the track.
        - artist:
            Name of the artist that created the song.
        - year:
            Song's year of release.
        - duration:
            Duration of the track in milliseconds.
        - explicit:
            Boolean that states whether the song contains swear words or not.
        - popularity:
            Popularity of the song. The higher the value, the more popular the song is. 0 represents the lowest
            popularity while 100 represnets the highest popularity.
        - danceability:
            Describes how suitable a track is for dancing based on a combination of musical elements including tempo,
            rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most
            danceable.
        - energy:
            Represents a perceptual measure of intensity and activity. A value of 0.0 represents the lowest energy and
            1.0 represents the highest energy.
        - loudness:
            The overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track and
            is the quality of a sound that is the primary psychological correlate of physical strength (amplitude).
            Values range between -60 and 10 db where -60 db is the quietest and 10 db is the loudest.
        - speechiness:
            Detects the presence of spoken words in a track. The more exclusively speech-like the
            recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value. Values above 0.66
            describe tracks that are probably made entirely of spoken words. Values between 0.33 and 0.66 describe
            tracks that may contain both music and speech, either in sections or layered, including such cases as rap
            music. Values below 0.33 most likely represent music and other non-speech-like tracks.
        - acousticness:
            A confidence measure from 0.0 to 1.0 of whether the track is acoustic. 0.0 represents low confidence the
            track is acoustic and 1.0 represents high confidence the track is acoustic.
        - instrumentalness:
            Predicts whether a track contains no vocals. "Ooh" and "aah" sounds are treated as instrumental in this
            context. Rap or spoken word tracks are clearly "vocal". The closer the instrumentalness value is to 1.0,
            the greater likelihood the track contains no vocal content. Values above 0.5 are intended to represent
            instrumental tracks, but confidence is higher as the value approaches 1.0.
        - valence:
            A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence
            sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative
            (e.g. sad, depressed, angry).
        - liveness:
            Detects the presence of an audience in the recording. Higher liveness values represent an increased
            probability that the track was performed live. A value above 0.8 provides strong likelihood that the track
            is live.
        - tempo:
            The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the
            speed or pace of a given piece and derives directly from the average beat duration.
        - key:
            The key the track is in. Integers map to pitches using standard Pitch Class notation. E.g. 0 = C, 1 = C♯/D♭,
            2 = D, and so on. If no key was detected, the value is -1.
        - mode:
            Mode indicates the modality (major or minor) of a track, the type of scale from which its melodic content
            is derived. Major is represented by 1 and minor is 0.

        Representation Invariants:
        - 0 <= self.popularity <= 100
        - 0.0 <= self.danceability <= 1.0
        - 0.0 <= self.energy <= 1.0
        - -60.0 <= self.loudness <= 10.0
        - 0.0 <= self.speechiness <= 1.0
        - 0.0 <= self.acousticness <= 1.0
        - 0.0 <= self.instrumentalness <= 1.0
        - 0.0 <= self.valence <= 1.0
        - 0.0 <= self.liveness <= 1.0
        - self.tempo >= 0
        - self.mode == 1 or self.mode == 0
        """
    name: str
    genre: str
    artist: str
    year: int
    duration: int
    explicit: bool
    popularity: int
    danceability: float
    energy: float
    loudness: float
    speechiness: float
    acousticness: float
    instrumentalness: float
    valence: float
    liveness: float
    tempo: float
    key: int
    mode: int


def read_and_write_csv(csv_file: str) -> None:
    """Reads data from the CSV file that the input refers to and loads it into a new CSV file
    called songs_final.csv. songs_final.csv will include only the songs and catergories we plan to use.

    Preconditions:
       - csv_file refers to a valid CSV file in the format described in the project proposal
    """
    with open(csv_file) as file:
        reader = csv.reader(file, delimiter=',')
