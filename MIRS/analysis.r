#!/usr/bin/Rscript
suppressMessages(library("tuneR"))

spectralCentroid <- function(spectrum, samplerate){
    freqbymag <- 0
    for(i in 1:length(spectrum)){
        freqbymag <- freqbymag + spectrum[i]*(i/length(spectrum)*samplerate)
    }
    #freqbymag <- sum(spectrum*(1:length(spectrum))/length(spectrum*samplerate))
    return(freqbymag/sum(spectrum))
}

spectralFlatness <- function(magnitudeSpectrum){
  geometricMean <- exp(mean(log(magnitudeSpectrum)))
  arithmeticMean <- mean(magnitudeSpectrum)
  return(geometricMean/arithmeticMean)
}

normalizedRMS <- function(waveform,bitDepth){
    return(sqrt(mean(waveform^2)))
}

args <- commandArgs(trailingOnly = TRUE)

waveform <- readWave(args[1])
waveform <- normalize(waveform)

spectrum <- abs(fft(waveform@left)[1:(length(waveform@left)/2)])

cat(
    c(
        length(waveform@left)/(waveform@samp.rate/1000),
        spectralCentroid(spectrum,waveform@samp.rate),
        spectralFlatness(spectrum),
        normalizedRMS(waveform@left)
    )
,'')