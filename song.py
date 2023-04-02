"""
CSC111 Winter 2023 Project:
MelodyMatch: Tailored Music Recommendations Derived From Your Spotify Habits

Module Description
==================

This Python module contains the Song class.

Contributors: Manaljav Munkhbayar, Kevin Hu, Stanley Pang, Jaeyong Lee.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
and faculty members who are part of CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2023 Manaljav Munkhbayar, Kevin Hu, Stanley Pang, Jaeyong Lee.
"""
from typing import Optional, Any

class Song:
    """An object that represents a specific song and stores its various song attributes.

        Instance Attributes
        - name:
            Name of the song.
        - genre:
            Genre of the track.
        - artist:
            Name of the artist that created the song.
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

        Representation Invariants:
        - 0.0 <= self.danceability <= 1.0
        - 0.0 <= self.energy <= 1.0
        - -60.0 <= self.loudness <= 10.0
        - 0.0 <= self.speechiness <= 1.0
        - 0.0 <= self.acousticness <= 1.0
        - 0.0 <= self.instrumentalness <= 1.0
        - 0.0 <= self.valence <= 1.0
        - 0.0 <= self.liveness <= 1.0
        """
    name: str
    danceability: float
    energy: float
    loudness: float
    speechiness: float
    acousticness: float
    instrumentalness: float
    valence: float
    liveness: float
    genre: str
    artist: str

    def __init__(self, name: str, danceability: float, energy: float, loudness: float, speechiness: float,
                 acousticness: float, instrumentalness: float, valence: float, liveness: float,
                 genre: Optional[str] = None, artist: Optional[str] = None) -> None:
        """Initialize a Song object"""

        self.name = name
        self.danceability = danceability
        self.energy = energy
        self.loudness = loudness
        self.speechiness = speechiness
        self.acousticness = acousticness
        self.instrumentalness = instrumentalness
        self.valence = valence
        self.liveness = liveness
        self.genre = genre
        self.artist = artist
