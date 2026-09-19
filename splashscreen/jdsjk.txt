import React, { useEffect, useMemo, useRef } from 'react';
import {
  View,
  Text,
  StatusBar,
  Animated,
  Dimensions,
} from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { APP_IMAGES } from '../assets/Assets';
import type { RootNavigationProp } from '../types/navigation';

const { width: SCREEN_WIDTH } = Dimensions.get('window');

interface Sector {
  icon: string;
  label: string;
}

interface SplashScreenProps {
  navigation: RootNavigationProp;
  onFinish?: () => void;
}

const SECTORS: readonly Sector[] = [
  { icon: '🏥', label: 'Health' },
  { icon: '📚', label: 'Education' },
  { icon: '🆘', label: 'Rescue' },
  { icon: '🤲', label: 'Welfare' },
  { icon: '🌊', label: 'Relief' },
  { icon: '🏗️', label: 'Housing' },
  { icon: '🌱', label: 'Livelihood' },
  { icon: '💧', label: 'Water' },
] as const;

const LOADER_DURATION = 3200;
const ANIMATION_DELAY = 180;
const SPRING_CONFIG = {
  toValue: 1,
  tension: 65,
  friction: 9,
  useNativeDriver: true,
};

const SplashScreen: React.FC<SplashScreenProps> = ({ navigation, onFinish }) => {
  const logoAnim = useRef(new Animated.Value(0)).current;
  const titleAnim = useRef(new Animated.Value(0)).current;
  const sectorsAnim = useRef(new Animated.Value(0)).current;
  const bottomAnim = useRef(new Animated.Value(0)).current;
  const loaderAnim = useRef(new Animated.Value(0)).current;

  const sectorWidth = useMemo(() => (SCREEN_WIDTH - 56 - 18) / 4, []);

  useEffect(() => {
    const animations = [
      Animated.spring(logoAnim, SPRING_CONFIG),
      Animated.spring(titleAnim, SPRING_CONFIG),
      Animated.spring(sectorsAnim, SPRING_CONFIG),
      Animated.spring(bottomAnim, SPRING_CONFIG),
    ];
    Animated.stagger(ANIMATION_DELAY, animations).start();

    Animated.timing(loaderAnim, {
      toValue: 1,
      duration: LOADER_DURATION,
      useNativeDriver: false,
    }).start();

    const timer = setTimeout(() => {
      onFinish?.();
      navigation.replace('Home');
    }, 3500);

    return () => clearTimeout(timer);
  }, [navigation, onFinish, logoAnim, titleAnim, sectorsAnim, bottomAnim, loaderAnim]);

  const createSlideUpAnimation = (anim: Animated.Value) => ({
    opacity: anim,
    transform: [{
      translateY: anim.interpolate({
        inputRange: [0, 1],
        outputRange: [24, 0],
      }),
    }],
  });

  const logoScale = logoAnim.interpolate({
    inputRange: [0, 1],
    outputRange: [0.7, 1],
  });

  const loaderWidth = loaderAnim.interpolate({
    inputRange: [0, 1],
    outputRange: ['0%', '100%'],
  });

  return (
    <SafeAreaView className="flex-1 bg-[#0060ae]" edges={['top', 'bottom']}>
      <StatusBar barStyle="light-content" backgroundColor="#0060ae" />

      <View className="flex-1 items-center justify-between pt-14 pb-12 px-7">

        <Animated.View style={createSlideUpAnimation(logoAnim)} className="w-full items-end">
          <View className="flex-row items-center gap-1.5 border border-white/25 rounded-full px-3 py-1.5">
            <View className="w-[5px] h-[5px] rounded-full bg-white/80" />
            <Text className="font-outfit-semibold text-[9px] text-white/80 tracking-[2px] uppercase">
              EST. 1990
            </Text>
          </View>
        </Animated.View>

        <View className="items-center">
          <Animated.View
            className="mb-7"
            style={{ opacity: logoAnim, transform: [{ scale: logoScale }] }}
          >
            <View className="w-[110px] h-[110px] rounded-[28px] bg-white/12 border border-white/20 items-center justify-center">
              <APP_IMAGES.LOGO width={72} height={72} />
            </View>
          </Animated.View>

          <Animated.View style={createSlideUpAnimation(titleAnim)} className="items-center">
            <Text className="font-outfit-extrabold text-[26px] text-white tracking-[0.5px] uppercase">
              AL<Text className="font-outfit-medium text-white/75">KHIDMAT</Text>
            </Text>
            <View className="flex-row items-center gap-2 my-2.5">
              <View className="w-9 h-px bg-white/30" />
              <View className="w-[5px] h-[5px] bg-white/70 rotate-45" />
              <View className="w-9 h-px bg-white/30" />
            </View>
            <Text className="font-outfit-regular text-[11px] text-white/65 tracking-[2.5px] uppercase">
              FOUNDATION PAKISTAN
            </Text>
            <Text className="font-outfit-light text-[12px] text-white/60 italic text-center mt-3.5 px-2.5 leading-5">
              "Service to Humanity with Integrity"
            </Text>
          </Animated.View>

          <Animated.View style={createSlideUpAnimation(sectorsAnim)} className="flex-row flex-wrap w-full mt-5 gap-1.5">
            {SECTORS.map((sector) => (
              <View
                key={sector.label}
                style={{ width: sectorWidth }}
                className="bg-white/10 border border-white/15 rounded-[10px] py-2 items-center gap-1"
              >
                <Text className="text-base leading-5">{sector.icon}</Text>
                <Text className="font-outfit-semibold text-[7.5px] text-white/70 tracking-[0.4px] uppercase text-center">
                  {sector.label}
                </Text>
              </View>
            ))}
          </Animated.View>
        </View>

        <Animated.View style={createSlideUpAnimation(bottomAnim)} className="items-center gap-3 w-full">
          <View className="w-[110px] h-0.5 bg-white/20 rounded-full overflow-hidden">
            <Animated.View
              className="h-full bg-white/80 rounded-full"
              style={{ width: loaderWidth }}
            />
          </View>
          <Text className="font-outfit-medium text-[8.5px] text-white/35 tracking-[3px] uppercase">
            LOADING
          </Text>
          <View className="flex-row items-center gap-2">
            <View className="w-6 h-px bg-white/15" />
            <Text className="font-outfit-medium text-[8px] text-white/20 tracking-[3px] uppercase">
              VERSION 1.0.0
            </Text>
            <View className="w-6 h-px bg-white/15" />
          </View>
        </Animated.View>
      </View>
    </SafeAreaView>
  );
};

export default SplashScreen;