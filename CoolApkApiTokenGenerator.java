import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Base64;
import java.util.Date;

public class CoolApkApiTokenGenerator {
    private static final String TOKEN = "token://com.coolapk.market/c67ef5943784d09750dcfbb31020f0ab?";
    private static final String DEVICE_ID = "00000000-0000-0000-0000-000000000000";
    private static final String PACKAGE_NAME = "com.coolapk.market";

    private static String bytesToHexString(byte[] bytes) {
        StringBuilder stringBuilder = new StringBuilder();
        for (byte b : bytes) {
            stringBuilder.append(String.format("%02x", b));
        }
        return stringBuilder.toString();
    }

    private static String md5(byte[] data) {
        try {
            MessageDigest messageDigest = MessageDigest.getInstance("MD5");
            byte[] md5 = messageDigest.digest(data);
            return bytesToHexString(md5);
        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException(e);
        }
    }

    private static byte[] base64Encode(byte[] data) {
        return Base64.getEncoder().encode(data);
    }

    private static String genTimestampMd5(long timestamp) {
        String timestampStr = String.valueOf(timestamp);
        return md5(timestampStr.getBytes());
    }

    public static String genToken() {
        long timestamp = new Date().getTime() / 1000;
        String salt = TOKEN + genTimestampMd5(timestamp) + "$" + DEVICE_ID + "&" + PACKAGE_NAME;
        byte[] encodedSalt = base64Encode(salt.getBytes());
        String saltMd5 = md5(encodedSalt);
        String hexTime = String.format("0x%x", timestamp);
        return saltMd5 + DEVICE_ID + hexTime;
    }
}
